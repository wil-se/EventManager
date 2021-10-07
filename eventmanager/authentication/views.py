from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import ThemeConfig
from reservation.models import *
from volley.models import *
from reservation.forms import SeatForm
import json


@login_required(login_url='/accounts/login/')
def main_render(request, page='overview.html', data={}):
    themeconfig = ""
    try:
        ThemeConfig.objects.filter(user=request.user)[0]
    except:
        themeconfig = ThemeConfig()
        themeconfig.name = "default generated"
        themeconfig.user = request.user
        themeconfig.save()

    return render(request, page, {**{
        'theme': themeconfig,
    }, **data})


@login_required(login_url='/accounts/login/')
def profile(request):

    return render_volley_manager_profile(request)
    


@login_required(login_url='/accounts/login/')
def render_volley_manager_profile(request):
    gymconfig = VolleyGymConf.objects.all().first()
    reservations = VolleyReservation.objects.all()
    canvas = gymconfig.get_canvases().first()

    seatform = SeatForm(initial={
        'canvas_width': canvas.width,
        'canvas_height': canvas.height,
        'canvases': canvas,
    })
    
    return main_render(request, page="profile.html", data={
        'seatform': seatform,
        'gymconfig': gymconfig,
        'reservations': reservations
    })


@login_required(login_url='/accounts/login/')
def get_canvas_config(request):
    place = Place.objects.filter(manager__pk=request.user).first()
    placeconfig = PlaceConfig.objects.filter(place=place).first()
    canvas = Canvas.objects.filter(placeconfig=placeconfig).first()

    seatconfig = SeatCanvasConfig.objects.filter(canvas=canvas)
    
    shapes = Shape.objects.filter(canvas=canvas)


    data = {
        'seats': {},
        'shapes': {},
    }

    data['canvas_width'] = canvas.width
    data['canvas_height'] = canvas.height

    for seat in seatconfig:
        print(seat.pk)
        print(seat)
        data['seats'][seat.seat.pk] = [seat.left, seat.top, seat.seat.radius]


    for shape in shapes:
        data['shapes'][shape.pk] = [shape.left, shape.top, shape.width, shape.height]

    print(data)


    return JsonResponse(data)




@login_required(login_url='/accounts/login/')
def set_canvas_config(request):
    data = json.loads(list(request.POST.keys())[0])
    canvas_width = data.get('canvas_width', None)
    canvas_height = data.get('canvas_height', None)
    canvas_id = data.get('canvas_id', None)
    seats = data.get('seats', None)
    shapes = data.get('shapes', None)

    canvas = Canvas.objects.get(pk=canvas_id)
    canvas.height = canvas_height
    canvas.width = canvas_width
    canvas.save()
    
    for seat in seats:
        try:
            seatcanvasconf = SeatCanvasConfig.objects.get(canvas=canvas, seat=seat)
            seatcanvasconf.left = seats[seat][0]
            seatcanvasconf.top = seats[seat][1]
            seatcanvasconf.save()
        except:
            seatcanvasconf = SeatCanvasConfig()
            seatcanvasconf.canvas = canvas
            seatcanvasconf.seat = Seat.objects.get(pk=seat)
            seatcanvasconf.left = seats[seat][0]
            seatcanvasconf.top = seats[seat][1]
            seatcanvasconf.save()

    for s in shapes:
        shape = Shape.objects.get(pk=s)
        shape.left = shapes[s][0]
        shape.top = shapes[s][1]
        shape.width = shapes[s][2]
        shape.height = shapes[s][3]
        shape.save()


    return JsonResponse({})



@login_required(login_url='/accounts/login/')
def add_user(request):
    return main_render(request, page='add_user.html', data={})



@login_required(login_url='/accounts/login/')
def save_user(request):
    username = request.POST.get('username', '')
    name = request.POST.get('name', '')
    last_name = request.POST.get('last_name', '')
    password = request.POST.get('password', '')
    password_two = request.POST.get('password_two', '')
    email = request.POST.get('email', '')
    email_two = request.POST.get('email_two', '')
    role = request.POST.get('role', '')
    print(username)
    txt = "\
        USERNAME: {}\n\
        NAME: {}\n\
        LAST_NAME: {}\n\
        PASSWORD1: {}\n\
        PASSWORD2 {}\n\
        SHUT UP! \n\
        EMAIL1: {}\n\
        EMAIL2: {}\n\
        ROLE: {}\n\
    ".format(username, name, last_name, password, password_two, email, email_two, role)
    
    print(txt)


    if not username \
        or not name \
        or not last_name \
        or not password_two \
        or not password_two \
        or not email \
        or not email_two:
        print("check 0")
        return JsonResponse({'success': False, 'message': "Sono richiesti tutti i campi"})    


    # controlla password uguali
    if password != password_two:
        print("check 1")
        return JsonResponse({'success': False, 'message': "Le password non coincidono"})    

    # controlla email uguali
    if email != email_two:
        print("check 2")
        return JsonResponse({'success': False, 'message': "Le email non coincidono"})    
            
    # controlla email già esistente
    if User.objects.filter(email=email).exists():
        print("email già presente")
        return JsonResponse({'success': False, 'message': "Email già presente"})    
        

    if role == "Admin":
        admin = User.objects.create_user(username, email, password)
        admin.first_name = name
        admin.last_name = last_name
        admin.save()
        print(admin)

    if role == "Manager":
        manager = VolleyManager.objects.create_user(username, email, password)
        manager.first_name = name
        manager.last_name = last_name
        manager.save()
        print(manager)

    return JsonResponse({'success': True})