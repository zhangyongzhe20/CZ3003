from django.db import models
# from backend.mazerunner.questions.models import Questions_teacher
# from backend.mazerunner.users.models import Student
# Create your models here.

class gameHistory(models.Model):

    worldID = models.IntegerField
    sectionID = models.IntegerField
    questionID = models.ForeignKey('questions.Questions_teacher', on_delete=models.CASCADE)
    studentID = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    timestamp = models.DateTimeField
    isAnsweredCorrect = models.BooleanField
    questionAnswer = models.CharField(max_length=30)
