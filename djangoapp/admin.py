from django.contrib import admin,auth
from django.contrib.auth import authenticate  
from django.contrib.auth.admin import UserAdmin  
from .forms import CustomUserCreationForm,SignupSubmitForm
from .models import Custom,Register
# Register your models here.

class formAdmin(admin.ModelAdmin):
    
    add_form = CustomUserCreationForm
    list_display = ['email','first_name','last_name','password','is_staff','is_active']


admin.site.register(Custom, formAdmin)



class formAdmins(admin.ModelAdmin):
    
    #add_form = SignupSubmitForm
    list_display = ['first_name','last_name','email','password','confirm_password','date','gender','country']


admin.site.register(Register, formAdmins)

