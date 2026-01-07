from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="chat-index"),
    path("message/", views.process_message, name="chat-message"),
]
