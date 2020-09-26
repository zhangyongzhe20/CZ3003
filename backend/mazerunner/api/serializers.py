from rest_framework import serializers
from users.models import User
from questions.models import Questions_teacher , Questions , Questions_answer , Questions_student
from gameHistory.models import questionHistory
from django.db.models import Count
## User




class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','email','name','distanceToNPC','overallScore','containBonus','role')

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
        print(obj.id)
        questionAnss = Questions_answer.objects.filter(questionID = obj.id)
        serializers = QuestionAnsSerializer(questionAnss , many = True)
        print(serializers.data)
        return serializers.data
    
    class Meta:
        model = Questions_teacher
        fields = ('id','questionBody', 'isMCQ' , 'questionAns')


class QuestionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = questionHistory
        fields = ('gameHistory','questionID','studentID','studentAnswer', 'isAnsweredCorrect')

    def create(self , validated_data):
        print(validated_data['questionID'].id)
        questionAns = Questions_answer.objects.get(questionID = validated_data['questionID'].id , isCorrect = True)
        qHistory = questionHistory(
            gameHistory = validated_data['gameHistory'],
            questionID = validated_data['questionID'],
            studentID = validated_data['studentID'],
            studentAnswer = validated_data['studentAnswer'],
            isAnsweredCorrect = (questionAns.questionText == validated_data['studentAnswer'])
        )
        qHistory.save()
        return qHistory


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
        fields = ('Ranking' , 'overallScore' , 'questionHistory')

    def get_questionHistory(self, obj):
        print(obj.id)
        qHistory = questionHistory.objects.values('gameHistory','questionID__questionLevel','isAnsweredCorrect').annotate(count=Count('isAnsweredCorrect')).order_by('gameHistory','questionID__questionLevel')
        print(qHistory)
        return qHistory

 