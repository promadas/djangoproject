from django.contrib import admin,auth

# Register your models here.
from .models import contact
class formAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'password']


admin.site.register(contact, formAdmin)
