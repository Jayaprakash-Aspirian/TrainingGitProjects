from django import forms
import re
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    firstname = forms.CharField(label="firstname", max_length=100)
    lastname = forms.CharField(label="lastname", max_length=100)
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data["password"]
        if not len(data) < 17 or not len(data) > 7:
            raise ValidationError("Password length must be between 8 to 16")
        elif not re.findall("[()[\]|\\`~!@#$%^&*_\-+=;:'\",<>./?]", data):
            raise ValidationError("atleast 1 special character needed!")
        return data

    def clean_email(self):
        data = self.cleaned_data["email"]
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(regex, data):
            return data
        else:
            raise ValidationError("Emailid is not valid")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not len(username) < 17 or not len(username) > 7:
            raise ValidationError("username length must be between 8 to 16")
        else:
            return username

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        regex = "^[6-9]\d{9}$"
        if re.search(regex, phone):
            return phone
        else:
            raise ValidationError("Not a valid phone number")


class UserLoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class SchoolAdminRegistrationForm(forms.Form):
    schoolname   = forms.CharField(label="schoolname", max_length=100)
    schooladdress= forms.CharField(label="schooladdress", max_length=100)   
    schooldistrict= forms.CharField(label="schooldistrict", max_length=20)
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data["password"]
        if not len(data) < 17 or not len(data) > 7:
            raise ValidationError("Password length must be between 8 to 16")
        elif not re.findall("[()[\]|\\`~!@#$%^&*_\-+=;:'\",<>./?]", data):
            raise ValidationError("atleast 1 special character needed!")
        print("p okay")
        return data

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not len(username) < 17 or not len(username) > 7:
            raise ValidationError("username length must be between 8 to 16")
        else:
            print("u okay")
            return username

   