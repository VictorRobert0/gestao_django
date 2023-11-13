from django import forms


# Create the form class.
class Usuario(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    password =  forms.IntegerField()