from django.shortcuts import render,redirect
from .login import LoginFormSubmitForm
from .models import contact
# Create your views here.
def login(request):
    
    if request.method == 'POST':
        
        form = LoginFormSubmitForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            
            return redirect(request.path_info)
        
        else:
            
            form = LoginFormSubmitForm()
            return redirect(request.path_info)
    
    
    else:
        form = LoginFormSubmitForm()
        
    context = {
        'form': form ,
        
        
    }
 
    return render(request, 'login.html',context) 
