from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record


class SingUpForm(UserCreationForm):
    # Email field
    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'Email address'
        }))
    # Frist name field
    first_name = forms.CharField(max_length=255, required=False, label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Frist name'
    }))
    # Last name field
    last_name = forms.CharField(max_length=255, required=True, label="", widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Last name'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        


class addRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Frist name",
            "class": "form-control"
        }),
        label=""
        )
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"Last name",
            "class": "form-control"
        }),
        label=""
    )
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"Email",
            "class": "form-control"
        }),
        label=""
    )
    phone_number = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"Phone",
            "class": "form-control"
        }),
        label=""
    )
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"Address",
            "class": "form-control"
        }),
        label=""
    )
    city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"City",
            "class": "form-control"
        }),
        label=""
    )
    state = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"State",
            "class": "form-control"
        }),
        label=""
    )
    zipcode = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                "placeholder":"Zipcode",
                "class": "form-control"
            }),
            label=""
    )
    
    class Meta:
        model = Record
        exclude = ('user',)