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


### QUESTION:


### GAME_HISTORY:


