from django import forms

class StudentFormClass(forms.Form):
    name=forms.CharField()
    roll_number=forms.IntegerField()
    percentage=forms.FloatField()
    
    