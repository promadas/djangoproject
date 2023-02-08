from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


# Create your models here.
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
country = (
    (0, 'Italy'),
    (1, 'Norway'),
    (2, 'Turkey'),
)
class Custom(AbstractUser):
    
    username = None
    email =models.EmailField(_('email_address'),unique=True,max_length=200)
    
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
       return self.email

class Register(models.Model):  
    first_name = models.CharField(_('email_address'),max_length=30)
    last_name = models.CharField(max_length=30)  
    email = models.EmailField(max_length=254,unique=True)  
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10,null=True)
    date = models.DateField(max_length=100,null=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,null=True)
    country = models.CharField(max_length=100,choices=country,null=True)
    
    def __str__(self):  
        return self.email
    

   