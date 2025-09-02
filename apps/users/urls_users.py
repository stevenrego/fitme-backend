from django.urls import path
from .views_users import me

urlpatterns = [
    path("me/", me, name="me"),
]
