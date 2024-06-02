from django import forms
from .models import Client, Licence

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'address', 'contact']  # Add other fields as needed

class LicenseForm(forms.ModelForm):
    class Meta:
        model = Licence
        fields = ['client', 'license_key', 'expiration_date']
