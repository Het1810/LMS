# forms.py

from django import forms
from datetime import timedelta
from django.forms.widgets import DateInput, Select
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, CreClients, CreClientLicense, CreLicenseStatus


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['nvarusername', 'nvarpassword']


class ClientForm(forms.ModelForm):
    nvarcontact = forms.IntegerField(label='Contact')   # Change to IntegerField

    class Meta:
        model = CreClients
        fields = ['nvarname', 'nvaremail', 'nvaraddress', 'nvarcontact']  # Add other fields as needed

    def clean_nvarcontact(self):
        nvarcontact = self.cleaned_data['nvarcontact']

        if not isinstance(nvarcontact, int):
            raise forms.ValidationError('Contact must be an integer.')

        return nvarcontact


class LicenceForm(forms.ModelForm):
    # intclientid = forms.ModelChoiceField(
    #     queryset=CreClients.objects.all(),
    #     label='Client ID',
    #     empty_label="Select a client",
    #     to_field_name='intid',  # Specify the field you want to display
    #     # widget=Select(attrs={'class': 'form-control select2'}),
    # )

    class Meta:
        model = CreClientLicense
        fields = ['nvarkey', 'intvalidity', 'bitactive', 'nvarreference', 'intremoteid', 'nvarremotepass']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the label for the intclientid field
        # self.fields['intclientid'].label_from_instance = lambda \
        #     obj: f"{obj.intid}"  # Adjust the field names

    def clean_nvarkey(self):
        return self.cleaned_data['nvarkey']

class LicencestatusForm(forms.ModelForm):
    class Meta:
        model = CreLicenseStatus
        fields = ['intlicenseid', 'nvarmacaddress', 'dtstartdate', 'dtenddate']

    dtstartdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'))

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get('dtstartdate')
        validity_days = self.instance.intlicenseid.intvalidity if self.instance.intlicenseid else 0

        # Calculate the end date
        end_date = start_date + timedelta(days=validity_days)
        cleaned_data['dtenddate'] = end_date

        return cleaned_data
