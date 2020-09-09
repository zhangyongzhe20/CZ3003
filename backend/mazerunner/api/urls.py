from django.urls import path
from .views import StudentAPIView , LoginAPIView ,LeaderBoardAPIView
urlpatterns = [
    path('api/student', StudentAPIView.as_view()),
    path('api/login', LoginAPIView.as_view()),
    path('api/leaderBoard', LeaderBoardAPIView.as_view())
]
