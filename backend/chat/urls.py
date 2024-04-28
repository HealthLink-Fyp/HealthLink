from django.urls import path
from . import views

urlpatterns = [
    path("calls/", views.CallView.as_view()),
    path("calls/transcript/", views.CallTranscriptView.as_view()),
    path("calls/emotion/", views.CallEmotionView.as_view()),
]
