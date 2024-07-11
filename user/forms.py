from django import forms
from django.forms import TextInput, EmailInput, PasswordInput, DateInput
from .models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control mt-2 w-100",
                "placeholder": "Informe o seu nome"
            }),
            "email": EmailInput(attrs={
                "class": "form-control mt-2 w-100",
                "placeholder": "Informe o seu email"
            }),
            "password": TextInput(attrs={
                "type": "password",
                "class": "form-control mt-2 w-100",
                "placeholder": "Informa a sua senha",
            }),
            "created_at": DateInput(attrs={
                "style": "display: none;",
            })
        }
        
        def clean_password(self):
            password = self.cleaned_data.get("password")
            if not password:
                self.add_error("value", "O campo da senha deve ser preenchido.")
            return password