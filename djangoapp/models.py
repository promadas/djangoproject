from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
 
from .manager import CustomUserManager



# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = None
    email =models.EmailField(('email_address'),unique=True,max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()  
      
def has_perm(self, perm, obj=None):  
        "Does the user have a specific permission?"  
        # Simplest possible answer: Yes, always  
        return True  
  
def is_staff(self):  
        "Is the user a member of staff?"  
        return self.staff  
  
@property  
def is_admin(self):  
        "Is the user a admin member?"  
        return self.admin  
  
def __str__(self):  
        return self.email  