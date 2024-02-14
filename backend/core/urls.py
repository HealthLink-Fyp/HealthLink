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
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("user", UserView.as_view()),
    path("refresh", RefreshView.as_view()),
    path("logout", LogoutView.as_view()),
    path("forget", ForgotView.as_view()),
    path("reset", ResetView.as_view()),
]
