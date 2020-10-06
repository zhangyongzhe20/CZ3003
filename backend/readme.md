# Backend Documentation

## 1. Software requirements:
* `python`: 3.7
* `django`: 2.2
* `RESTful API`: rest_framework
* `Database`: sqlite


## 2. Overall Backend Structure:
The Django application that uses Unity as a front end. It needs an API to allow Unity to consume data from the database.
![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/blob/master/backend/docs/structure.jpeg)


## 3. RESTful APIs: 
* API Routes: Route the incoming HTTP request from frontend to the API controllers
* API Serializers: Map models to Json for get & post requests

#### 3.1. API routes:
``` python 
urlpatterns = [
    path('api/login/',LoginAPIView.as_view(), name = 'login'),
    path('api/students', StudentAPIView.as_view() , name = 'students'),
    path('api/students/leaderboard', LeaderBoardAPIView.as_view() , name = 'leaderboard'),
    path('api/questions', QuestionAPIView.as_view() , name = 'questions'),
    path('api/questions/create', CreateQuestionAPIView.as_view() , name = 'create-questions'),
    path('api/gameSummary', gameSummaryAPIView.as_view() , name = 'gameSummary')
]
```

#### 3.2. API Serializers: Each route has corresponding serializers
*  Route: api/login/
``` python 
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self , data):
        student = authenticate(**data)
        if student:
            return student
        raise serializers.ValidateError("Incorrect Email/Password")
```

* Route: api/students
``` python
class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','email','name','distanceToNPC','overallScore','containBonus','role')
```

* Route: api/students/leaderboard
``` python 
class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name' , 'overallScore')
```

* Route: api/questions
``` python 

class QuestionTeacherSerializer(serializers.ModelSerializer):
    questionAns = serializers.SerializerMethodField()

    def get_questionAns(self, obj):
        questionAnss = Questions_answer.objects.filter(questionID = obj.id)
        serializers = QuestionAnsSerializer(questionAnss , many = True)
        return serializers.data
    
    class Meta:
        model = Questions_teacher
        fields = ('id','questionBody' , 'questionAns')
```

* Route: api/gameSummary
``` python
## Game Summary
class gameSummarySerializer(serializers.ModelSerializer):
    questionHistory = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('email', 'overallScore' , 'questionHistory')

```


## 4. Models:
Each model is a Python class that subclasses django.db.models.Model, which is used to map all atributes of a model to a table stored in database.

#### 4.1.USER:
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


#### 4.2. QUESTION:
Three sub-models under QUESTION:

1. Teachers' questions
``` python
class Questions_teacher(Questions):
    worldID =  models.ForeignKey(World, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    questionLevel = models.IntegerField(default=0)

    def __str__(self):
        return self.questionBody
```

2. Student-proposed questions
```python
class Questions_student(Questions):
    Proposer = models.CharField(max_length=100)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.questionBody
```

3. Answers of questions
```python
class Questions_answer(models.Model):
    #multiple possible foreign keys reference (question_teacher or question_student)?
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=200)
    isCorrect = models.BooleanField(default=False)
    def __str__(self):
        return str(self.questionID) + "-" + self.questionText
```

#### 4.3. GAME_HISTORY:
Foreign keys are used to link to model QUESTION, USER
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


## 5. API Controllers
The controller responds to the user input and performs interactions on the data model objects. The controller receives the input, optionally validates it and then passes the input to the model.

#### 5.1. Account Controller
``` python
#Login
class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []
    def post(self , request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            student = serializer.validated_data
            token, created = Token.objects.get_or_create(user=student)
            return Response({
                "user" : StudentAccountSerializer(student).data,
                "token": token.key
                })
        except:
            return Response({"Error Message" : "Incorrect Email/Password"},status = status.HTTP_401_UNAUTHORIZED)
    
class StudentAPIView(APIView):
    serializer_class = StudentAccountSerializer
    def get_queryset(self):
        users = User.objects.all()
        return users
    def get(self , request):
        try:
            id = request.query_params["id"]
            if id != None:
                student = User.objects.get(id = id)
                serializer = StudentAccountSerializer(student)
        except:
                students = User.objects.filter(is_staff = False)
                serializer = StudentAccountSerializer(students , many = True)    
        return Response(serializer.data)
```

#### 5.2. Leaderboard Controller
``` python 
class LeaderBoardAPIView(APIView):
    serializer_class = LeaderBoardSerializer
    def get(self , request):
        students = User.objects.filter(is_staff = False)
        serializer = LeaderBoardSerializer(students , many = True)
        return Response(serializer.data)
```

#### 5.3. Question Controller
``` python 
class QuestionAPIView(APIView):
    def get(self , request):
        try:
            world = World.objects.get(name = request.data['world'])
            section = Section.objects.get(name = request.data['section'])
            role = 'no role'
            if(request.data["role"] == "1"):
                role = 'project manager'
            if(request.data["role"] == "2"):
                role = 'frontend'
            if(request.data["role"] == "3"):
                role = 'backend'
            questions = Questions_teacher.objects.filter(worldID = world , sectionID  = section , role = role, questionLevel = request.data["questionLevel"] )   
            serializer = QuestionTeacherSerializer(questions , many = True)
            return Response(serializer.data , status = status.HTTP_200_OK)
        except:
            return Response({'Error Message' :'Please enter the correct input'} ,status = status.HTTP_400_BAD_REQUEST)
    def post(self, request):  
        try: 
            world = World.objects.get(name = request.data['world'])
            section = Section.objects.get(name = request.data['section'])
            data = {
            "worldID" : world.id,
            "sectionID" : section.id,
            "questionID": request.data['questionID'],
            "studentID" : request.data['studentID'],
            "studentAnswer" : request.data['studentAnswer'],
            "isAnsweredCorrect" : request.data['isAnsweredCorrect'],
            }
            serializer = QuestionHistorySerializer(data = data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(({'pass': True}) , status = status.HTTP_201_CREATED)
        except:        
            return Response({'pass': False},status = status.HTTP_400_BAD_REQUEST)

class CreateQuestionAPIView(APIView):
    def post(self , request):
        serializer = QuestionStudentSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'submitted': True} , status = status.HTTP_201_CREATED)
        return Response({'submitted':False},status = status.HTTP_400_BAD_REQUEST)
```

#### 5.4. Game Controller
``` python 
class gameSummaryAPIView(APIView):
    def get(self , request):
        try:
            student = User.objects.get(email = request.data['email'])
            serializer= gameSummarySerializer(student)
            return Response(serializer.data , status = status.HTTP_200_OK)   
        except:
            return Response({'Error Message': 'record not found'} , status = status.HTTP_400_BAD_REQUEST)
```



