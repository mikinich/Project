from django.urls import path
from .views import my_login, profile, my_logout


urlpatterns = [
    path("login/", my_login, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", my_logout, name="logout"),
]
