from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.models import User
from .serializers import LoginSerializer ,StudentAccountSerializer ,QuestionTeacherSerializer, QuestionHistorySerializer, QuestionStudentSerializer, gameSummarySerializer , LeaderBoardSerializer
from questions.models import Questions_teacher , Questions , Questions_answer
from gameHistory.models import World , Section
from rest_framework.authtoken.models import Token
# Create your views here.


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
            return Response({"Error Message" : "Incorrect Email/Password"})
    


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
        
    def post(self , request):
        serializer = StudentAccountSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class LeaderBoardAPIView(APIView):
    serializer_class = LeaderBoardSerializer
    def get(self , request):
        students = User.objects.filter(is_staff = False)
        serializer = LeaderBoardSerializer(students , many = True)
        return Response(serializer.data)

class QuestionAPIView(APIView):
    def get(self , request):
       
        try:
            if request.data["world"] != None and request.data["section"] != None and request.data["role"] !=None and request.data["questionLevel"] != None:
                questions = Questions_teacher.objects.filter(world = request.data["world"], section  = request.data["section"], role = request.data["role"], questionLevel = request.data["questionLevel"] )   
        except:
            questions = Questions_teacher.objects.all()
        serializer = QuestionTeacherSerializer(questions , many = True)
        return Response(serializer.data)

    def post(self, request):   
        print(request.data)
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
        print(data)
        serializer = QuestionHistorySerializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(({'pass': True}) , status = status.HTTP_201_CREATED)
        return Response({'pass': False},status = status.HTTP_400_BAD_REQUEST)

class CreateQuestionAPIView(APIView):
    def post(self , request):
        print(request.data)
        serializer = QuestionStudentSerializer(data = request.data)
        print(serializer.is_valid())
        if(serializer.is_valid()):
            serializer.save()
            return Response({'submitted': True} , status = status.HTTP_201_CREATED)
        return Response({'submitted':False},status = status.HTTP_400_BAD_REQUEST)

class gameSummaryAPIView(APIView):
    def get(self , request):
        try:
            student = User.objects.get(account = request.data['account'])
            print(student)
            serializer= gameSummarySerializer(student)
            return Response(serializer.data)   
        except:
            return Response({'Error Message': 'record not found'})
        

