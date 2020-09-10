from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.models import User , Student
from .serializers import UserAccountSerializer,StudentAccountSerializer,StudentAccountLeaderBoardSerializer , QuestionTeacherSerializer, QuestionHistorySerializer, QuestionStudentSerializer
from questions.models import Questions_teacher , Questions , Questions_answer
# Create your views here.

class StudentAPIView(APIView):
    def get(self , request):
        students = Student.objects.all()
        serializer = StudentAccountSerializer(students , many = True)
        return Response(serializer.data)
    def post(self , request):
        serializer = StudentAccountSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self , request): 
        try:
            student = Student.objects.get(account = request.data['account'] , password = request.data['password'])
            print(request.data)
            serializer = StudentAccountSerializer(student)
            return Response(serializer.data)   
        except:
            return Response({'Error Message': 'incorrect username/password'})
    

class LeaderBoardAPIView(APIView):
    def get(self , request):
        students = Student.objects.all()
        serializer = StudentAccountLeaderBoardSerializer(students , many = True)
        return Response(serializer.data)
    

class QuestionAPIView(APIView):
    def get(get , request):
            print(request.data)
            questions = Questions_teacher.objects.filter(world = request.data['world'], section  = request.data['section'],
            role = request.data['role'], questionLevel = request.data['questionLevel'])    
            serializer = QuestionTeacherSerializer(questions , many = True)
            return Response(serializer.data)
    def post(self, request):
        serializer = QuestionHistorySerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'pass': True} , status = status.HTTP_201_CREATED)
        return Response({'pass':False},status = status.HTTP_400_BAD_REQUEST)

#class CreateQuestionAPIView(APIView):