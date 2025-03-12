from django.urls import path
from .views import latest_post

urlpatterns = [
    path("latest/", latest_post, name="latest_post"),
]