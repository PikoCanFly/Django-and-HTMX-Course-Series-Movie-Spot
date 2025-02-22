from django.urls import path
from .views import Login, RegisterUser, Logout, profile, create_list

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("create_list/", create_list, name="create_list")
]