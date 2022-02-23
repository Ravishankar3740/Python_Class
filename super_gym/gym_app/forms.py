from django import forms
from .models import Enquiryuser

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email_Id = forms.EmailField()
    phone_no = forms.CharField(max_length=255)
    Address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    details = forms.CharField(max_length=10,required=False)

    class Meta:
        model = Enquiryuser
        fields = ["username","email_Id","phone_no","Address","city"]

   