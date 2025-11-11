from django.urls import path
from .views import RegisterView
from django.urls import path, include

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("api/auth/", include("users.urls")),
]