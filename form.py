from django import forms
from django.forms import fields
#from django.db.models import fields
from employee.models import newReg,addEmp

class regForm(forms.ModelForm):
    class Meta:
        model = newReg
        fields ="__all__"

class empForm(forms.ModelForm):
    class Meta:
        model = addEmp
        fields = "__all__"