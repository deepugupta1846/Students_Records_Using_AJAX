from django import forms
from .models import *


class insertform(forms.ModelForm):
    class Meta:
        model = Srecord
        fields = ['Sname', 'Fname', 'Gender', 'Clas', 'Rollno']
        widgets = {
            'Sname' : forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'Fname': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'Gender': forms.Select(attrs={'class': 'form-control mb-2'}),
            'Clas': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'Rollno': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }