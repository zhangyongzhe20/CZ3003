from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    # facebook: FACEBOOK
    # Twitter: TWITTER
    class Meta:
        abstract = True



class Student(User):
    distanceToNPC = models.IntegerField(default = 0)
    overallScore= models.IntegerField(default = 0)
    Ranking = models.IntegerField(default = 0)
    containBonus = models.BooleanField(default = False)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.name