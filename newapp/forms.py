from django import forms
from newapp.models import Bus
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'
        widgets = {
            'bus_no':forms.TextInput(attrs={'class': 'form-control'}),
            'bus_name': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'bus_type': forms.Select(attrs={'class': 'form-select'}),
            'arrival_time': forms.TimeInput(attrs={'class': 'form-control','type': 'time','placeholder': 'HH:MM AM/PM'}),
            'departure_time': forms.TimeInput(attrs={'class': 'form-control','type': 'time','placeholder': 'HH:MM AM/PM'}),
        }
     
        
class CustomUserCreationForm(UserCreationForm):
    phone_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$', 
        message="Enter a valid 10-digit mobile number"
    )
    mobile_number = forms.CharField(validators=[phone_regex],widget=forms.TextInput(attrs={'class': 'form-control '}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control '}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control '}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','mobile_number','password1','password2']


