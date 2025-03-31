from django.contrib import admin
from .models import BloodSugarReading, InsulinInjection

admin.site.register(BloodSugarReading)
admin.site.register(InsulinInjection)