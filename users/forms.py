from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserList
from django.forms import ModelForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1","password2")

class CreateListForm(ModelForm):
    class Meta:
        model = UserList
        fields = ("name",)