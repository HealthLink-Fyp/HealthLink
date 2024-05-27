from django.urls import path
from .views import transcript, chat, call

urlpatterns = [
    # Call URLs
    path("calls/", call.CallView.as_view()),
    path("calls/emotion/", call.CallEmotionView.as_view()),
    # LLM URLs
    path("calls/transcript/", transcript.CallTranscriptView.as_view()),
    # Chat URLs
    path("chat/", chat.ChatView.as_view()),
]
