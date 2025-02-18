from django import forms
from .models import StartaProject,Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = StartaProject
        fields = ['name', 'email', 'mobile', 'description']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'location', 'phone_number']