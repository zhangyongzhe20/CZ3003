from django.db import models
from questions.models import Questions_teacher , World , Section
from users.models import User
# Create your models here.


class questionHistory(models.Model):
    worldID = models.ForeignKey(World, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section , on_delete=models.CASCADE)
    questionID = models.ForeignKey(Questions_teacher, on_delete=models.CASCADE)
    studentID = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    isAnsweredCorrect = models.BooleanField(default=False)
    studentAnswer = models.CharField(max_length=200, default ="1")

    def __str__(self):
        return 'question record: ' + str(self.questionID)