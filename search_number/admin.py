from django.contrib import admin
from .models import People


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']


admin.site.register(People, PersonAdmin)
