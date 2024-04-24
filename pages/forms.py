from django import forms
from .models import Contact, CustomUser
from django.core import validators
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class SignUpForm(UserCreationForm):
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = CustomUser
        fields = ['email']

    def clean_password2(self):   # Shu yerda nafaqat password, barcha qismlarini validate qilish uchun clean methodini ishlatish mumkin edi.
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Parolingiz confirmationdan o'tmadi!")
        return data['password2']