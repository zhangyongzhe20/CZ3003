from django.urls import path
from django.conf.urls import url
from .views import StudentAPIView , QuestionAPIView ,CreateQuestionAPIView , gameSummaryAPIView  , LoginAPIView , LeaderBoardAPIView

urlpatterns = [
    path('api/login/',LoginAPIView.as_view()),
    path('api/students/leaderboard', LeaderBoardAPIView.as_view()),
    path('api/students', StudentAPIView.as_view()),
    path('api/questions', QuestionAPIView.as_view()),
    path('api/questions/create', CreateQuestionAPIView.as_view()),
    path('api/gameSummary', gameSummaryAPIView.as_view())
]
