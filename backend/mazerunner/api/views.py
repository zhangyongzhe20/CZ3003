from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Count, Max, Min, Avg
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.models import User
from .serializers import LoginSerializer ,StudentAccountSerializer ,QuestionTeacherSerializer, QuestionHistorySerializer, QuestionStudentSerializer, gameSummarySerializer , LeaderBoardSerializer, overallSummarySerializer
from questions.models import Questions_teacher , Questions , Questions_answer
from gameHistory.models import World , Section, questionHistory
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
import statistics
from django.http.response import HttpResponseRedirect
from .forms import signupForm

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
        
class LeaderBoardAPIView(APIView):
    serializer_class = LeaderBoardSerializer
    def get(self , request):
        students = User.objects.filter(is_staff = False).order_by("overallScore")
        serializer = LeaderBoardSerializer(students , many = True)
        return Response(serializer.data)

class QuestionAPIView(APIView):
    def post(self , request):
        try:
            print(request.data)
            world = World.objects.get(name = request.data['world'])
            section = Section.objects.get(name = request.data['section'])

            role = 'no role'
            if(request.data["role"] == "1"):
                role = 'project manager'
            if(request.data["role"] == "2"):
                role = 'frontend'
            if(request.data["role"] == "3"):
                role = 'backend'
            print(role)
            if(int(request.data["questionLevel"])  == 1):
                questions = Questions_teacher.objects.filter(worldID = world , sectionID  = section , role = role, questionLevel = request.data["questionLevel"] ).order_by('?')[:5]   
            else:
                questions = Questions_teacher.objects.filter(worldID = world , sectionID  = section , role = role, questionLevel = request.data["questionLevel"] ).order_by('?')[:3]  
            serializer = QuestionTeacherSerializer(questions , many = True)
            return Response(serializer.data , status = status.HTTP_200_OK)
        except:
            return Response({'Error Message' :'Please enter the correct input'} ,status = status.HTTP_400_BAD_REQUEST)


class QuestionSubmitAPIView(APIView):
    def post(self, request):  
        try: 
            world = World.objects.get(name = request.data['world'])
            section = Section.objects.get(name = request.data['section'])
            point = int(request.data['pointGain'])
            print(point)
            data = {
            "worldID" : world.id,
            "sectionID" : section.id,
            "questionID": request.data['questionID'],
            "studentID" : request.data['studentID'],
            "studentAnswer" : request.data['studentAnswer'],
            "isAnsweredCorrect" : request.data['isAnsweredCorrect'],
            }
            student = User.objects.get(id = request.data['studentID'])
            serializer = QuestionHistorySerializer(data = data)
            if serializer.is_valid() and student!= None:
                serializer.save()
                student.overallScore = student.overallScore + point
                student.save()
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

class gameSummaryAPIView(APIView):
    def get(self , request):
        try:
            student = User.objects.get(email = request.data['email'])
            serializer= gameSummarySerializer(student)
            return Response(serializer.data , status = status.HTTP_200_OK)   
        except:
            return Response({'Error Message': 'record not found'} , status = status.HTTP_400_BAD_REQUEST)

class overallSummaryView(APIView):
    """
    View for Dashboard

    Returns:
        HttpResponse: Response that contains all the variables used by dashboard.html template
    """
    authentication_classes = []
    permission_classes = []
    def get(self,request):
        currObjects = dict()
        noParams = True

        if "studentID" in request.query_params.keys():
            currObjects["Student"] = request.query_params["studentID"]
        else:
            currObjects["Student"] = None

        if "worldID" in request.query_params.keys():
            currObjects["World"] = request.query_params["worldID"]
            noParams = False
        else:
            currObjects["World"] = None

        if "sectionID" in request.query_params.keys():
            currObjects["Section"] = request.query_params["sectionID"]
            noParams = False
        else:
            currObjects["Section"] = None
        
        if "questionID" in request.query_params.keys():
            currObjects["Question"] = request.query_params["questionID"]
            noParams = False
        else:
            currObjects["Question"] = None
        
        if currObjects["Student"] != None:
            queryset = questionHistory.objects.filter(studentID__name = currObjects["Student"])
            noParams = False
        else:
            queryset = questionHistory.objects.all()

        if queryset.count() == 0:
            return render(request, 'dashboard.html', {
                'data': None
            })

        objList = dict()

        labels = ['Correct', 'Incorrect']
        data = [0, 0]
        backgroundColor = ['#2A9D8F', '#F4A261']

        objList["World"] = [str(x["worldID__name"]) for x in queryset.order_by().values("worldID__name").distinct()]
        
        if currObjects["World"] != None:
            queryset = queryset.filter(worldID__name = currObjects["World"])
            objList["Section"] = [str(x["sectionID__name"]) for x in queryset.order_by().values("sectionID__name").distinct()]
            if currObjects["Section"] != None:
                queryset = queryset.filter(sectionID__name = currObjects["Section"])
                objList["Question"] = [str(x["questionID__questionLevel"]) for x in queryset.order_by().values("questionID__questionLevel").distinct()]
                if currObjects["Question"] != None:
                    queryset = queryset.filter(questionID__questionLevel = currObjects["Question"])

        studentList = [str(x["studentID__name"]) for x in queryset.order_by().values("studentID__name").distinct()]

        studentScore = list(queryset.filter(isAnsweredCorrect=True).values('studentID__name').annotate(Count('studentID__name')))
        studentScore = {x['studentID__name']: x['studentID__name__count'] for x in studentScore}

        tempScore = studentScore
        for student in studentList:
            if student not in studentScore.keys():
                tempScore[student] = 0
        studentScore = tempScore

        orderedStudentList = [k for k, v in sorted(studentScore.items(), key=lambda item: [1])]
        orderedScoreList = [v for k, v in sorted(studentScore.items(), key=lambda item: [1])]

        scoreLevel = dict()
        scoreLevel["Max"] = max(orderedScoreList)
        scoreLevel["Min"] = min(orderedScoreList)
        scoreLevel["Mean"] = round(statistics.mean(orderedScoreList), 2)
        scoreLevel["Median"] = statistics.median(orderedScoreList)

        
        data[0] = queryset.filter(isAnsweredCorrect=True).count()
        data[1] = queryset.count() - data[0]
    
        return render(request, 'dashboard.html', {
            'labels': labels,
            'data': data,
            'backgroundColor': backgroundColor,
            'currObjects': currObjects,
            'objList': objList,
            'noParams': noParams,
            'studentScore': studentScore,
            'orderedStudentList': orderedStudentList,
            'orderedScoreList': orderedScoreList,
            'scoreLevel': scoreLevel
        })

class signup(APIView):
    """
    View for Signup form

    Returns:
        HttpResponse: Response that contains all the variables used by sign_up.html template
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        form = signupForm()

        return render(request, 'sign_up.html', {
            'form': form
        })
    
    def post(self, request):
        form = signupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if form.cleaned_data['is_admin']:
                User.objects.create_superuser(email, password)
            elif password == '':
                User.objects.create_user(email)
            else:
                User.objects.create_user(email, password)
            return HttpResponseRedirect('/')
        
        return render(request, 'sign_up.html', {
            'form': form
        })
