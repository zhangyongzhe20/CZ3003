from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from questions.models import Questions_teacher , Questions , Questions_answer , Questions_student
from gameHistory.models import questionHistory 
from django.db.models import Count , F


## User
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self , data):
        student = authenticate(**data)
        if student:
            return student
        raise serializers.ValidateError("Incorrect Email/Password")

class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','email','name','distanceToNPC','overallScore','containBonus','role')
        
class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name' , 'overallScore')
##Question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Questions
        fields = ('id','questionBody', 'isMCQ')

class QuestionAnsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Questions_answer
        fields = ('questionText', 'isCorrect')


class QuestionTeacherSerializer(serializers.ModelSerializer):
    questionAns = serializers.SerializerMethodField()

    def get_questionAns(self, obj):
        questionAnss = Questions_answer.objects.filter(questionID = obj.id)
        serializers = QuestionAnsSerializer(questionAnss , many = True)
        return serializers.data
    
    class Meta:
        model = Questions_teacher
        fields = ('id','questionBody', 'isMCQ' , 'questionAns')


    
class QuestionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = questionHistory
        fields = ('worldID' , 'sectionID','questionID','studentID','studentAnswer', 'isAnsweredCorrect')


class QuestionStudentSerializer(serializers.ModelSerializer):
    questionAns = QuestionAnsSerializer(many = True)
    class Meta:
        model = Questions_student
        fields = QuestionSerializer.Meta.fields + ('Proposer', 'isApproved' , 'questionAns')
    
    def create(self , validated_data):
        datas = validated_data.pop('questionAns')
        questionStudent = Questions_student.objects.create(**validated_data)
        for data in datas:
            Questions_answer.objects.create(questionID = questionStudent , **data)
        return questionStudent

## Game Summary
class gameSummarySerializer(serializers.ModelSerializer):
    questionHistory = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('email', 'overallScore' , 'questionHistory')

    def get_questionHistory(self, obj):
        qHistory= questionHistory.objects.values('worldID__name','sectionID__name','questionID__questionLevel').annotate( world = F('worldID__name') ,
        section = F('sectionID__name') , questionLevel = F('questionID__questionLevel'), value=Count('questionID__questionLevel')).values('world','section','questionLevel','value')        
        for data in qHistory:
            correctCount =  questionHistory.objects.filter(worldID__name = data['world'] , sectionID__name = data['section'] , questionID__questionLevel = data['questionLevel'], isAnsweredCorrect = True).count()
            data['value'] = str(correctCount) + " / " +  str(data['value']) 
        return list(qHistory)

 
 


  