from django.db import models

# Create your models here.

class User(models.Model):

    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    # facebook: FACEBOOK
    # Twitter: TWITTER
    isAdmin = models.BooleanField

class Student(User):

    #check
    isAdmin = models.BooleanField(default=False)

    distanceToNPC = models.IntegerField
    overallScore: models.IntegerField
    Ranking = models.IntegerField
    containBonus = models.BooleanField
    role = models.CharField(max_length=30)