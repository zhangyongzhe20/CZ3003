from django.db import models

# Create your models here.
class Questions(models.Model):
    questionBody = models.CharField(max_length=200)
    questionType = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Questions_teacher(Questions):
    world = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    questionLevel = models.IntegerField

class Questions_student(Questions):
    Proposer = models.CharField(max_length=30)
    isApproved = models.BooleanField

class Questions_answer(Questions):
    #multiple possible foreign keys reference (question_teacher or question_student)?
    questionID = models.ForeignKey(Questions_teacher, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=200)
    isCorrect = models.BooleanField
