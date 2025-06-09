from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


# class StudentRegisterForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_student = True
#         if commit:
#             user.save()
#         return user
