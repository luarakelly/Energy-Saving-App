from django.contrib.auth.forms import UserCreationForm #it is a built in form
from django.contrib.auth.models import User #it is built in model
from django import forms #describes a form from djangos alredy made forms and determines how it works and appears. form class’s fields map to HTML form <input> elements.
from .models import Kitchen #for timeline preview with records
from .models import UserProfile

class SignUp(UserCreationForm):
    #adding filds that are not present in the model
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Adress'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    #to overwrite the attributes from the fields that alredy exists in djangos user creation html form:
    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

#additional fields for users to fill in on the profile page
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'state', 'cep')
        #just adding custumization to the Html form
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
        }

class KitchenForm(forms.ModelForm):
    class Meta:
        model = Kitchen
        fields = ['appliance', 'quantity', 'brand', 'model', 'hour_use_day', 'times_week']