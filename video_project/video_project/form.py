from django import forms
from django.contrib.auth.models import User 
 
class ContactForm(forms.Form):
    fullname = forms.CharField(
                    widget = forms.TextInput(
                                attrs = {
                                            "class":"form-control", 
                                            "id":"form_full_name", 
                                            'placeholder': "Enter name"
                                        }
                                )
                )
    email = forms.EmailField(
                    widget = forms.EmailInput(
                                attrs = {
                                            "class": "form-control", 
                                            "id":"email",
                                            'placeholder': "enter your email "
                                        }
                                )
                )
    content = forms.CharField(
                    widget = forms.Textarea(
                        attrs = {
                            'class': 'form-control',
                            'placeholder': "enter your message"
                        }
                    )
                )
    
    #custom Validation

    def clean_email(self):
        email = self.cleaned_data.get("email") 
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
                    widget = forms.TextInput(
                                attrs = {
                                    'class': "form-control",
                                    'id': "form_login",
                                    'placeholder': 'Enter Name'
                                }
                    )
                );

    password = forms.CharField(
                    widget = forms.PasswordInput(
                        attrs = {
                            'class' : 'form-control',
                            'id': 'form_password',
                            'placeholder': 'Enter Password'
                        }
                    )
                );



class RegisterForm(forms.Form):
    username = forms.CharField(
                    widget = forms.TextInput(
                            attrs = {
                                'class': 'form-control',
                                'id': "form_login",
                                'placeholder' : 'Enter username'
                            }
                    )
                )

    email = forms.EmailField( 
                    widget = forms.EmailInput(
                        attrs = {
                            'class': 'form-control',
                            'id': 'form_login',
                            'placeholder': 'Enter Email'
                        }
                    )
                )

    password = forms.CharField(
                    widget = forms.PasswordInput(
                        attrs = {
                            'class': "form-control",
                            'id': 'form_password',
                            'placeholder': "Enter password"
                        }
                    )
                )
    password2 = forms.CharField(
                    label = "Confirm Password",
                    widget = forms.PasswordInput(
                        attrs = {
                            'class': "form-control",
                            'id': 'confirm_password',
                            'placeholder': "Re-enter your password"
                        }
                    )
                )

    #custom Validation

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already exits")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already exits")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password does not match with confirm password")
        return data