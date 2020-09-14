from rest_framework import serializers
from users.models import Student , User
from questions.models import Questions_teacher , Questions , Questions_answer , Questions_student
from gameHistory.models import questionHistory
from django.db.models import Count
## User
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('account', 'password', 'name')

    def create(self , validated_data):
        user = User(
            account = validated_data['account'],
            password = validated_data['password'],
            name = validated_data['name']
        )
        user.save()
        return user
        
    def update(self , instance , validated_data):
        instance.account = validated_data.get('account', instance.account)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = UserAccountSerializer.Meta.fields + ('distanceToNPC','overallScore','Ranking','containBonus','role')


## LeaderBoard
class StudentAccountLeaderBoardSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = ('Ranking' , 'name' , 'overallScore' , 'containBonus')


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
        fields = ('gameHistory','questionID','studentID','isAnsweredCorrect','studentAnswer')
    

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

class gameSummarySerializer(serializers.ModelSerializer):
    questionHistory = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ('Ranking' , 'overallScore' , 'questionHistory')

    def get_questionHistory(self, obj):
        print(obj.id)
        qHistory = questionHistory.objects.values('gameHistory','questionID__questionLevel','isAnsweredCorrect').annotate(count=Count('isAnsweredCorrect'))
        print(qHistory)
        return qHistory

 