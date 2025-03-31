from django.contrib import admin
from .models import BloodSugarRecord, InsulinInjection

admin.site.register(BloodSugarRecord)
admin.site.register(InsulinInjection)