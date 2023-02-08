from django.contrib import admin
from django.urls import path
from djangoapp import views

app_name = 'djangoapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.sign_up,name='sign_up'),
    #path('login/',views.log_in,name='login_page'),
    #path('profile/',views.profile,name='profile'),
]
