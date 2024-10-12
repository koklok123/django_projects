from django.contrib import admin
from .models import Basesettings, Employees, Blog

admin.site.register(Basesettings)
admin.site.register(Employees)
admin.site.register(Blog)
