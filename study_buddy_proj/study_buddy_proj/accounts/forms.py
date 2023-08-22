from django.forms import ModelForm
from django.contrib.auth import forms as auth_forms, get_user_model

User = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(auth_forms.AuthenticationForm):
    class Meta:
        fields = ('username', 'password')


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'bio', 'avatar')
