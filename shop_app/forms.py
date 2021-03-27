from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class AddAddressForm(forms.Form):
    """Form for adding another address to the account."""
    line1 = forms.CharField(label='name or company', max_length=125)
    line2 = forms.CharField(label='street and number', max_length=125)
    postcode = forms.CharField(label='post code', max_length=10)
    city = forms.CharField(label='city', max_length=125)
    country = forms.CharField(label='country', max_length=64)
    phone = forms.IntegerField(label='phone number')


class CheckoutForm(forms.Form):
    name = forms.CharField(required=False)
    street = forms.CharField(required=False)
    apartment = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    city = forms.CharField(required=False)
    zip = forms.CharField(required=False)
