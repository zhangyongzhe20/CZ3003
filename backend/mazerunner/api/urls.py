from django.urls import path
from django.conf.urls import url
from .views import StudentAPIView , LoginAPIView  , QuestionAPIView ,CreateQuestionAPIView , gameSummaryAPIView 
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('api/students', StudentAPIView.as_view()),
    path('api/login', LoginAPIView.as_view()),
    path('api/questions', QuestionAPIView.as_view()),
    path('api/questions/create', CreateQuestionAPIView.as_view()),
    path('api/gameSummary', gameSummaryAPIView.as_view())
]
