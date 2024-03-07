from django.urls import path

from core.views.profile import ProfileView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
]
