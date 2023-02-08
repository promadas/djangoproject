from django.shortcuts import render,redirect,HttpResponse
from .forms import SignupSubmitForm

from django.contrib.auth import login,logout,authenticate
from .models import Custom,Register

# Create your views here.


def sign_up(request):
    
    detail_list = Register.objects.all().values()
    if request.method == 'POST':
        fm = SignupSubmitForm(request.POST)
        if fm.is_valid():
            fm.save()
            
            #return redirect(log_in)
        
    else:
        fm = SignupSubmitForm()
        return render(request,'sign_up.html',{'form':fm, 'details':detail_list})
    
'''   
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
