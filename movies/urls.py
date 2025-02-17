from django.urls import path
from .views import landing_page, movie_detail

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("movie/<int:movie_id>", movie_detail, name="movie_detail")
]