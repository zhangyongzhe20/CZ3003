from django.db import models
# Create your models here.

class World(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.CharField(max_length=70,blank = True)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=70, blank = True)
    def __str__(self):
        return self.name


class Questions(models.Model):
    questionBody = models.CharField(max_length=200)
     # class Meta:
    #     abstract = True

class Questions_teacher(Questions):
    worldID =  models.ForeignKey(World, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    questionLevel = models.IntegerField(default=0)

    def __str__(self):
        return self.questionBody


class Questions_student(Questions):
    Proposer = models.CharField(max_length=100)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.questionBody

class Questions_answer(models.Model):
    #multiple possible foreign keys reference (question_teacher or question_student)?
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=200)
    isCorrect = models.BooleanField(default=False)
    def __str__(self):
        return str(self.questionID) + "-" + self.questionText
