from django import forms
from .models import Student, Professor

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['index', 'firstname', 'lastname', 'email', 'image']

class RegisterProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['firstname', 'lastname', 'email', 'image']