from django.urls import path
from .views import StudentAPIView , LoginAPIView
urlpatterns = [
    path('api/student', StudentAPIView.as_view()),
    path('api/login', LoginAPIView.as_view()),
]
