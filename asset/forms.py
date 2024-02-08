from .models import *
from django import forms 
from django.forms import ModelForm, DateInput,TimeInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This form will be used for registration of company along with CompanyForm
class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

# This form will be used for registration of company along with userForm
class CompanyForm(ModelForm):

    class Meta:
        model = CompanyInformation
        exclude = ("user",)

# This form will be used to create list of employees
class EmployeeForm(ModelForm):
    

    class Meta:
        model = EmployeeInformation
        exclude = ("company",)

# This form will be used to assign asset to an employee
class AssetAssignForm(ModelForm):

    class Meta:
        model = AssetTrack
        exclude = ("company","employee","return_date","return_time","return_condition","return_condition_log","status",)

        widgets = {
            'assign_date': DateInput(attrs={'type': 'date'}),
            'assign_time': TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            "name": "Asset name",
            "category": "Asset Category",
        }
        
        
# This form will be used to update assigned asset of an employee
class AssetUpdateForm(ModelForm):

    class Meta:
        model = AssetTrack
        exclude = ("company",)
        
        widgets = {
            'assign_date': DateInput(attrs={'type': 'date'}),
            'assign_time': TimeInput(attrs={'type': 'time'}),
            'return_date': DateInput(attrs={'type': 'date'}),
            'return_time': TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            "name": "Asset name",
            "category": "Asset Category",
        }
    def clean(self):
        cleaned_data = super(AssetUpdateForm, self).clean()
        assign_date = self.cleaned_data.get('assign_date')
        return_date = self.cleaned_data.get('return_date')
        if return_date < assign_date:
            raise forms.ValidationError("Return date should be greater than Assign or delegated date.")
        return cleaned_data    