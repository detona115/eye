from django.contrib import admin

# Register your models here.
from .models import Event, Data, Form

admin.site.register(Event)
admin.site.register(Data)
admin.site.register(Form)
