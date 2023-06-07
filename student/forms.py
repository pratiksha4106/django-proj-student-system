from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Student_ID','first_name','last_name','email','percentage']
    
        labels = {
        'Student_ID':'Student ID Number',
        'first_name':'First Name',
        'last_name':'Last Name',
        'email':'Email',
        'percentage':'Percentage'
        }

        widges = {
        'Student_ID':forms.NumberInput(attrs={'class': 'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'percentage':forms.NumberInput(attrs={'class':'form-control'}),
        }


