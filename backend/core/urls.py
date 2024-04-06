from django.urls import path

from core.views.authentication import (
    RegisterView,
    LoginView,
    UserView,
    RefreshView,
    LogoutView,
    ForgotView,
    ResetView,
)
from core.views.profile import ProfileView
from core.views import choice

urlpatterns = [
    # views/authentication
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/user/", UserView.as_view(), name="user"),
    path("auth/refresh/", RefreshView.as_view(), name="refresh"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/forgot/", ForgotView.as_view(), name="forgot"),
    path("auth/reset/", ResetView.as_view(), name="reset"),
    # views/profile
    path("auth/profile/", ProfileView.as_view(), name="profile"),
    # views/choice
    path("choices/", choice.ProfileChoiceView.as_view(), name="choice"),
]
