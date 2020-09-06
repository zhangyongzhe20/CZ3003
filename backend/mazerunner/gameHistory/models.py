from django.db import models

# Create your models here.

class gameHistory(models.Model):

    worldID = models.IntegerField
    sectionID = models.IntegerField
    questionID = models.ForeignKey('Questions_teacher', on_delete=models.CASCADE)
    studentID = models.ForeignKey('Student', on_delete=models.CASCADE)
    timestamp = models.DateTimeField
    isAnsweredCorrect = models.BooleanField

    #do we need this?
    questionAnswer = models.CharField(max_length=30)
