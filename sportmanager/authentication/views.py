from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ThemeConfig

@login_required(login_url='/accounts/login/')
def main_render(request, page='dashboard.html', data={}):
    themeconfig = ThemeConfig.objects.filter(user=request.user)[0]
    print(themeconfig.navbar)
    return render(request, page, {**{
        'theme': themeconfig,
    }, **data})