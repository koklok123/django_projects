from django.shortcuts import render
from apps.settings.models import Basesettings, Employees, Blog
# Create your views here.



def settings(request):
    try:
        setting = Basesettings.objects.latest('id')
    except Basesettings.DoesNotExist:
        setting = None 

    employ = Employees.objects.all().order_by('?')[:4]
    blog = Blog.objects.all().order_by('?')[:3]

    return render(request, 'index.html', locals())

