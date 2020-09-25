from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields =('type', 'price', 'status', 'description')


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields =('type', 'price', 'status', 'description')



class phoneForm(forms.ModelForm):
    class Meta:
        model = phone
        fields =('type', 'price', 'status', 'description')

