'''from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomUserCreationForm

from django.contrib.auth import login,logout,authenticate
from .models import CustomUser

# Create your views here.


def sign_up(request):
    
    detail_list = CustomUser.objects.all().values()
    if request.method == 'POST':
        fm = CustomUserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            
            #return redirect(log_in)
        
    else:
        fm = CustomUserCreationForm()
        return render(request,'sign_up.html',{'form':fm, 'details':detail_list})
        
        
def log_in(request):
    
    if request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect(profile)
        
        else:
           return HttpResponse("Username or password is incorrect")
        
    else:
        return render(request,'log_in.html')
    

def profile(request):
    return render(request,'profile.html')


'''