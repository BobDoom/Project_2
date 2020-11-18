from django.contrib import admin

# Register your models here.
from .models import Event  # Импортируем модуль

admin.site.register(Event)