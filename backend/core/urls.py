from django.urls import path

from .views import authentication, choice, profile

urlpatterns = [
    # views/authentication
    path("auth/register/", authentication.RegisterView.as_view(), name="register"),
    path("auth/login/", authentication.LoginView.as_view(), name="login"),
    path("auth/user/", authentication.UserView.as_view(), name="user"),
    path("auth/refresh/", authentication.RefreshView.as_view(), name="refresh"),
    path("auth/logout/", authentication.LogoutView.as_view(), name="logout"),
    path("auth/forget/", authentication.ForgotView.as_view(), name="forget"),
    path("auth/reset/", authentication.ResetView.as_view(), name="reset"),
    path("auth/profile/", profile.ProfileView.as_view(), name="profile"),
    # views/choice
    path("choices/", choice.ProfileChoiceView.as_view(), name="choice"),
]
