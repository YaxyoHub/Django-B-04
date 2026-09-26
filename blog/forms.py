from django import forms
from .models import Student

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'image',
            'ism',
            'familiya',
            'yosh',
            'manzil',
            'is_active'
        ]

    
