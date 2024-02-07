from .models import *
from django.forms import ModelForm, DateTimeInput, DateInput,TimeInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        
class CompanyForm(ModelForm):

    class Meta:
        model = CompanyInformation
        exclude = ("user",)

class EmployeeForm(ModelForm):

    class Meta:
        model = EmployeeInformation
        exclude = ("user",)