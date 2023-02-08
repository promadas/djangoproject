from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django import forms
from .models import Custom,Register
from django.contrib.auth import get_user_model


User = get_user_model()  
  
class CustomUserCreationForm(UserCreationForm):  
  
    password1 = forms.CharField(widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  
  
    class Meta:  
        model = Custom  
        fields = ('email', )  
      
    def clean_email(self):  
        email = self.cleaned_data.get('email')  
        qs = User.objects.filter(email=email)  
        if qs.exists():  
            raise forms.ValidationError("Email is taken")  
        return email  
  
    def clean(self):  
        '''  
        Verify both passwords match.  
        '''  
        cleaned_data = super().clean()  
        password1 = cleaned_data.get("password1")  
        password2 = cleaned_data.get("password2")  
          
        if password1 is not None and password1 != password2:  
            self.add_error("password2", "Your passwords must match")  
        return cleaned_data  
  
    def save(self, commit=True):  
        # Save the provided password in hashed format  
        user = super().save(commit=False)  
        user.set_password(self.cleaned_data["password1"])  
        if commit:  
            user.save()  
        return user          
      
      
class SignupSubmitForm():
    
    email = forms.EmailField(max_length=200,help_text='Required')
    class Meta:
        
        model = Register
        fields = ('first_name','last_name','email','password','confirm_password','date','gender','country')