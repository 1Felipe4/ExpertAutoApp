from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms.models import ModelChoiceField
from .models import Manufacturer, Pic, Vehicle 

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [ 'email', 'first_name', 'last_name',  'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Retype Password'})

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Password'
        }
))


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('pics', 'documents')

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['model'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['selling_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['manufacturer'].widget.attrs.update({'class': 'form-control'})
        self.fields['engine'].widget.attrs.update({'class': 'form-control'})        
        self.fields['chassis_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['engine_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['manufacture_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['engine_and_trans'].widget.attrs.update({'class': 'form-control'})
        self.fields['interior'].widget.attrs.update({'class': 'form-control'})
        self.fields['exterior'].widget.attrs.update({'class': 'form-control'})
        self.fields['suspension'].widget.attrs.update({'class': 'form-control'})
        self.fields['safety'].widget.attrs.update({'class': 'form-control'})
        self.fields['other_features'].widget.attrs.update({'class': 'form-control'})
        


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model =  Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super( ManufacturerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['pic'].widget.attrs.update({'class': 'custom-file-input', 'type':'file'})

class AttachmentPicForm(forms.ModelForm):
    class Meta:
        model =  Pic
        fields = ("file",)

    def __init__(self, *args, **kwargs):
        super( AttachmentPicForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'custom-file-input', 'type':'file'})


def get_industries():
    all = ((-1, "All Manufacturers"),) + tuple(Manufacturer.objects.filter(profile__isnull=False).values_list('pk', 'name'))
    return all




class VehicleBasicFilterForm(forms.ModelForm):
    manufacturer =  ModelChoiceField(queryset=Manufacturer.objects.filter(vehicle__isnull=False), empty_label="All Manufacturers", required=False)
    model = forms.CharField( max_length=255, required=False)
    class Meta:
            fields = [
                'chassis_no',
                'model',
                'manufacturer',
            ]
            model = Vehicle

    def __init__(self, *args, **kwargs):
            super(VehicleBasicFilterForm, self).__init__(*args, **kwargs)
            self.fields['chassis_no'].widget.attrs.update({'class': 'form-control', 'type': 'search', 'placeholder': 'Chassis #'})
            self.fields['model'].widget.attrs.update({'class': 'form-control', 'type': 'search', 'placeholder': 'Model'})
            self.fields['manufacturer'].widget.attrs.update({'class': 'form-control', 'type': 'search'})            