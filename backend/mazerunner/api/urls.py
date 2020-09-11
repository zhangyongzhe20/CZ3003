from django.urls import path
from .views import StudentAPIView , LoginAPIView ,LeaderBoardAPIView , QuestionAPIView ,CreateQuestionAPIView , gameSummaryAPIView
urlpatterns = [
    path('api/student', StudentAPIView.as_view()),
    path('api/login', LoginAPIView.as_view()),
    path('api/leaderBoard', LeaderBoardAPIView.as_view()),
    path('api/questions', QuestionAPIView.as_view()),
    path('api/questions/create', CreateQuestionAPIView.as_view()),
    path('api/gameSummary', gameSummaryAPIView.as_view())
]
