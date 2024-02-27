from django.urls import path

from .views import (
    ForgotView,
    LoginView,
    LogoutView,
    RefreshView,
    RegisterView,
    ResetView,
    UserView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("user/", UserView.as_view(), name="user"),
    path("refresh/", RefreshView.as_view(), name="refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("forget/", ForgotView.as_view(), name="forget"),
    path("reset/", ResetView.as_view(), name="reset"),
]
