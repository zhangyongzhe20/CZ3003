from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        students = User.objects.filter(is_staff = False)
        serializer = LeaderBoardSerializer(students , many = True)
        return Response(serializer.data)

class QuestionAPIView(APIView):
    def get(self , request):
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

class gameSummaryAPIView(APIView):
    def get(self , request):
        try:
            student = User.objects.get(email = request.data['email'])
            serializer= gameSummarySerializer(student)
            return Response(serializer.data , status = status.HTTP_200_OK)   
        except:
            return Response({'Error Message': 'record not found'} , status = status.HTTP_400_BAD_REQUEST)
class overallSummaryView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request):
        try:
            currWorld = request.query_params["worldID"]
            queryset = questionHistory.objects.filter(worldID__name = currWorld)
        except:
            currWorld = None
            queryset = questionHistory.objects.all()
        data = []
        labels = []
        backgroundColor = []
        worldSet = set()

        print(currWorld)
        labels = ['Correct', 'Incorrect']
        data = [0, 0]
        backgroundColor = ['#2A9D8F', '#F4A261']
        for question in queryset:
            worldSet.add(question.worldID.name)
            if question.isAnsweredCorrect:
                data[0] += 1
            else:
                data[1] += 1

        worldList = World.objects.all()
        
        if currWorld == None:
            currWorld = worldList[0]
    
        return render(request, 'dashboard.html', {
            'labels': labels,
            'data': data,
            'backgroundColor': backgroundColor,
            'worldList': worldList,
            'currWorld': currWorld
        })

   

def selectWorld(request, worldID):
    currWorld = worldID
