from authentication.views import main_render


def reservation(request):
    return main_render(request, 'reservation.html', {})