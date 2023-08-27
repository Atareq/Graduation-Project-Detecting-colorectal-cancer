from django import forms
from .models import TestResult

class TestForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = '__all__' 
        exclude = ['user','test_result'] 

    