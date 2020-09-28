from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.models import User
from .serializers import LoginSerializer ,StudentAccountSerializer ,QuestionTeacherSerializer, QuestionHistorySerializer, QuestionStudentSerializer, gameSummarySerializer
from questions.models import Questions_teacher , Questions , Questions_answer
from rest_framework.authtoken.models import Token
# Create your views here.


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


#Login
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

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
    
    

class QuestionAPIView(APIView):
    def get(self , request):
            print(request.data)
            questions = Questions_teacher.objects.filter(world = request.data['world'], section  = request.data['section'],
            role = request.data['role'], questionLevel = request.data['questionLevel'])    
            serializer = QuestionTeacherSerializer(questions , many = True)
            return Response(serializer.data)
    def post(self, request):    
        serializer = QuestionHistorySerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(({'pass': serializer.data['isAnsweredCorrect']}) , status = status.HTTP_201_CREATED)
        return Response({'Error Message': 'Unable to insert new record'},status = status.HTTP_400_BAD_REQUEST)

class CreateQuestionAPIView(APIView):
    def post(self , request):
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
        

