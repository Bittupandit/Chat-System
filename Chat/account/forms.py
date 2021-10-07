from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
import datetime
class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','password1','password2','dob','contact']
        widgets = {
            'dob':DateInput(),
        }

    def __int__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['name'].required = True

    def clean_date(self):
        dob = self.cleaned_data['dob']
        if dob >= datetime.date.today():
            raise forms.ValidationError("The date cannot be in the future!")
        return dob

    def save(self,commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.dob = self.cleaned_data['dob']
        user.contact = self.cleaned_data['contact']
        if commit:
            user.save()
        return user


