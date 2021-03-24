from django import forms


class LoginForm(forms.Form):
    """Form for logging in."""
    username = forms.CharField(label="username", max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    """Form for creating an account."""
    username = forms.CharField(label='username', max_length=64)
    email = forms.CharField(label='email', max_length=64, widget=forms.EmailInput())
    password = forms.CharField(label='password', max_length=64, widget=forms.PasswordInput())
    line1 = forms.CharField(label='name or company', max_length=125)
    line2 = forms.CharField(label='street and number', max_length=125)
    postcode = forms.CharField(label='post code', max_length=10)
    city = forms.CharField(label='city', max_length=125)
    country = forms.CharField(label='country', max_length=64)
    phone = forms.IntegerField(label='phone number')


class AddAddressForm(forms.Form):
    """Form for adding another address to the account."""
    line1 = forms.CharField(label='name or company', max_length=125)
    line2 = forms.CharField(label='street and number', max_length=125)
    postcode = forms.CharField(label='post code', max_length=10)
    city = forms.CharField(label='city', max_length=125)
    country = forms.CharField(label='country', max_length=64)
    phone = forms.IntegerField(label='phone number')
