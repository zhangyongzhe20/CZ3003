# Backend Documentation
 This repo serves the development of backend for CZ3003


## Software requirements:
* `python`: 3.7
* `django`: 2.2
* `RESTful API`: Djago_restframework
* `Database`: sqlite


## Models:
Each model is a Python class that subclasses django.db.models.Model, which is used to map all atributes of a model to a table stored in database.

### USER:
``` python
class User(AbstractBaseUser):  
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    distanceToNPC = models.IntegerField(default = 0)
    overallScore= models.IntegerField(default = 0)
    containBonus = models.BooleanField(default = False)
    role = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
```
Authentication:
Auto generate a token when a new user is created
``` python 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    Token.objects.get_or_create(user=instance)
```
UserManager class:
To create student or teacher account

```python
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.save(using=self._db)
        return user
```


### QUESTION:
Three sub-models under QUESTION:
1. Teachers' questions
2. Student-proposed questions
3. Answers of questions

``` python
class Questions_teacher(Questions):
    worldID =  models.ForeignKey(World, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    questionLevel = models.IntegerField(default=0)

    def __str__(self):
        return self.questionBody
```

```python
class Questions_student(Questions):
    Proposer = models.CharField(max_length=100)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.questionBody
```

```python
class Questions_answer(models.Model):
    #multiple possible foreign keys reference (question_teacher or question_student)?
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=200)
    isCorrect = models.BooleanField(default=False)
    def __str__(self):
        return str(self.questionID) + "-" + self.questionText
```



### GAME_HISTORY:
The play record:
Foreign keys:
1. questionID (link to which question is played)
2. studentID  (link to which student played)
3. world & section (link to which senario is played)

``` python 
class questionHistory(models.Model):
    worldID = models.ForeignKey(World, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section , on_delete=models.CASCADE)
    questionID = models.ForeignKey(Questions_teacher, on_delete=models.CASCADE)
    studentID = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    isAnsweredCorrect = models.BooleanField(default=False)
    studentAnswer = models.CharField(max_length=30, default ="1")
```






