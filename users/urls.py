from django.urls import path
from .views import Login, RegisterUser, Logout, profile, create_list, delete_list, add_to_list, list_detail, delete_movie

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("create_list/", create_list, name="create_list"),
    path("delete_list/<int:list_id>", delete_list, name="delete_list"),
    path("lists/<int:list_id>/add/<int:movie_id>/<str:movie_name>", add_to_list, name="add_to_list"),
    path("list/<int:list_id>", list_detail, name="list_detail"),
    path("delete/<int:movie_id>/<int:list_id>", delete_movie, name="delete_movie")
]