from django.urls import path
from .views import face_recognition_view

urlpatterns = [
    path('face-recognition/', face_recognition_view, name='face_recognition'),
]