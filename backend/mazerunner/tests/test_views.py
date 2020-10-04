from django.urls import reverse,resolve
from rest_framework.test import APITestCase, URLPatternsTestCase , APIClient
from rest_framework.authtoken.models import Token
from users.models import User
from gameHistory.models import questionHistory
from questions.models import Questions_teacher ,Questions_answer , World , Section
from api.serializers import StudentAccountSerializer , LeaderBoardSerializer , QuestionTeacherSerializer ,gameSummarySerializer
import json
# Create your tests here.

class TestViews(APITestCase): 
    
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('login')
        self.leaderboard_url = reverse('leaderboard')
        self.students_url = reverse('students')
        self.questions_url = reverse('questions')
        self.create_questions_url= reverse('create-questions')
        self.game_summary_url = reverse('gameSummary')
    
        self.credentials = {
            'email': 'testuser@mail.com',
            'password': 'password',
            'name' : 'testuser',
            'role' : 'testing role'
             }
        self.user = User.objects.create_user(**self.credentials)
        
        world1 = World.objects.create(name = "1")
        world2 = World.objects.create(name = "2")

        section1 = Section.objects.create(name = "1")   
        section2 = Section.objects.create(name = "2")

        question1 = Questions_teacher.objects.create(
            questionBody = "1+1 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section1,
            role = "testing role",
            questionLevel = 1)
        Questions_answer.objects.create(questionID = question1,questionText = "1",isCorrect = False)
        Questions_answer.objects.create(questionID = question1,questionText = "2",isCorrect = True)
        Questions_answer.objects.create(questionID = question1,questionText = "3",isCorrect = False)
        Questions_answer.objects.create(questionID = question1,questionText = "4",isCorrect = False)

        self.question = question1

        question2 = Questions_teacher.objects.create(
            questionBody = "2+2 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section1,
            role = "testing role",
            questionLevel = 1)
        Questions_answer.objects.create(questionID = question2,questionText = "1",isCorrect = False)
        Questions_answer.objects.create(questionID = question2,questionText = "2",isCorrect = False)
        Questions_answer.objects.create(questionID = question2,questionText = "3",isCorrect = False)
        Questions_answer.objects.create(questionID = question2,questionText = "4",isCorrect = True)

        questionHistory.objects.create(worldID = question2.worldID , sectionID = question2.sectionID , questionID = question2,
         studentID = self.user , isAnsweredCorrect  = True , studentAnswer = '4' )   

        question3 = Questions_teacher.objects.create(
            questionBody = "1*1 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section2,
            role = "testing role",
            questionLevel = 1)
        Questions_answer.objects.create(questionID = question3,questionText = "1",isCorrect = True)
        Questions_answer.objects.create(questionID = question3,questionText = "2",isCorrect = False)
        Questions_answer.objects.create(questionID = question3,questionText = "3",isCorrect = False)
        Questions_answer.objects.create(questionID = question3,questionText = "4",isCorrect = False)

        questionHistory.objects.create(worldID = question3.worldID , sectionID = question3.sectionID , questionID = question3,
         studentID = self.user , isAnsweredCorrect  = False , studentAnswer = '4' )  

        question4 = Questions_teacher.objects.create(
            questionBody = "2*2 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section2,
            role = "testing role",
            questionLevel = 1)
        Questions_answer.objects.create(questionID = question4,questionText = "1",isCorrect = False)
        Questions_answer.objects.create(questionID = question4,questionText = "2",isCorrect = False)
        Questions_answer.objects.create(questionID = question4,questionText = "3",isCorrect = False)
        Questions_answer.objects.create(questionID = question4,questionText = "4",isCorrect = True)

        questionHistory.objects.create(worldID = question4.worldID , sectionID = question4.sectionID , questionID = question4,
         studentID = self.user , isAnsweredCorrect  = True , studentAnswer = '4' ) 

        question5 = Questions_teacher.objects.create(
            questionBody = "10+10 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section1,
            role = "testing role",
            questionLevel = 2)
        Questions_answer.objects.create(questionID = question5,questionText = "10",isCorrect = False)
        Questions_answer.objects.create(questionID = question5,questionText = "20",isCorrect = True)
        Questions_answer.objects.create(questionID = question5,questionText = "30",isCorrect = False)
        Questions_answer.objects.create(questionID = question5,questionText = "40",isCorrect = False)

        questionHistory.objects.create(worldID = question5.worldID , sectionID = question5.sectionID , questionID = question5,
         studentID = self.user , isAnsweredCorrect  = False , studentAnswer = '40' ) 

        question6 = Questions_teacher.objects.create(
            questionBody = "10+20 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section1,
            role = "testing role",
            questionLevel = 2)
        Questions_answer.objects.create(questionID = question6,questionText = "10",isCorrect = False)
        Questions_answer.objects.create(questionID = question6,questionText = "20",isCorrect = False)
        Questions_answer.objects.create(questionID = question6,questionText = "30",isCorrect = True)
        Questions_answer.objects.create(questionID = question6,questionText = "40",isCorrect = False)

        questionHistory.objects.create(worldID = question6.worldID , sectionID = question6.sectionID , questionID = question6,
         studentID = self.user , isAnsweredCorrect  = True , studentAnswer = '30' ) 

        question7 = Questions_teacher.objects.create(
            questionBody = "10*10 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section2,
            role = "testing role",
            questionLevel = 2)
        Questions_answer.objects.create(questionID = question7,questionText = "100",isCorrect = True)
        Questions_answer.objects.create(questionID = question7,questionText = "200",isCorrect = False)
        Questions_answer.objects.create(questionID = question7,questionText = "300",isCorrect = False)
        Questions_answer.objects.create(questionID = question7,questionText = "400",isCorrect = False)

        questionHistory.objects.create(worldID = question7.worldID , sectionID = question7.sectionID , questionID = question7,
         studentID = self.user , isAnsweredCorrect  = True , studentAnswer = '100' ) 

        question8 = Questions_teacher.objects.create(
            questionBody = "20*10 = ?",
            isMCQ = True,
            worldID = world1,
            sectionID = section1,
            role = "testing role",
            questionLevel = 2)
        Questions_answer.objects.create(questionID = question8,questionText = "100",isCorrect = False)
        Questions_answer.objects.create(questionID = question8,questionText = "200",isCorrect = True)
        Questions_answer.objects.create(questionID = question8,questionText = "300",isCorrect = False)
        Questions_answer.objects.create(questionID = question8,questionText = "400",isCorrect = False)

        questionHistory.objects.create(worldID = question8.worldID , sectionID = question8.sectionID , questionID = question8,
         studentID = self.user , isAnsweredCorrect  = True , studentAnswer = '200' ) 

        question9 = Questions_teacher.objects.create(
            questionBody = " x + y = ?",
            isMCQ = True,
            worldID = world2,
            sectionID = section1,
            role = "testing role",
            questionLevel = 1)
        Questions_answer.objects.create(questionID = question9,questionText = "x",isCorrect = False)
        Questions_answer.objects.create(questionID = question9,questionText = "x+y",isCorrect = True)
        Questions_answer.objects.create(questionID = question9,questionText = "y",isCorrect = False)
        Questions_answer.objects.create(questionID = question9,questionText = "y",isCorrect = False)

        questionHistory.objects.create(worldID = question9.worldID , sectionID = question9.sectionID , questionID = question9,
         studentID = self.user , isAnsweredCorrect  = False , studentAnswer = 'x' ) 

        question10 = Questions_teacher.objects.create(
            questionBody = "y+x = ?",
            isMCQ = True,
            worldID = world2,
            sectionID = section1,
            role = "testing role",
            questionLevel = 2)
        Questions_answer.objects.create(questionID = question10,questionText = "x",isCorrect = False)
        Questions_answer.objects.create(questionID = question10,questionText = "x+y",isCorrect = True)
        Questions_answer.objects.create(questionID = question10,questionText = "y",isCorrect = False)
        Questions_answer.objects.create(questionID = question10,questionText = "x",isCorrect = False)
        
        questionHistory.objects.create(worldID = question10.worldID , sectionID = question10.sectionID , questionID = question10,
        studentID = self.user , isAnsweredCorrect  = False , studentAnswer = 'x' ) 

    #Login 
    def test_user_login_with_no_data(self):
        res = self.client.post(self.login_url)
        self.assertEqual(res.status_code , 401)
    
    def test_user_login_with_correct_data(self):
        res = self.client.post(self.login_url,self.credentials , format='json')
        token, created = Token.objects.get_or_create(user=self.user)
        res_data = json.loads(res.content)
        self.assertEqual(res_data , {'user': StudentAccountSerializer(self.user).data , 'token' : token.key},)
        self.assertEqual(res.status_code , 200)
    
    def test_user_login_with_wrong_data(self):
        res = self.client.post(self.login_url,{'email':'testuser@mail.com','password':'wrong-password'},format='json')
        self.assertEqual(res.status_code , 401)


    # Get Student
    def test_get_student_withoutQuery(self):
        self.client.force_authenticate(user =self.user)
        res = self.client.get(self.students_url)
        res_data = json.loads(res.content)

        students = User.objects.filter(is_staff = False)

        self.assertEqual(res.status_code , 200)
        self.assertEqual(res_data , StudentAccountSerializer(students , many = True).data)
        
    def test_get_student_withQuery(self):
        self.client.force_authenticate(user =self.user)
        res = self.client.get(self.students_url , {'id' :self.user.id}, content_type='application/json')
        res_data = json.loads(res.content)

        student = User.objects.get(id = self.user.id)

        self.assertEqual(res.status_code , 200)
        self.assertEqual(res_data , StudentAccountSerializer(student).data)

    #leaderboard
    def test_get_leaderboard(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.leaderboard_url)
        res_data = json.loads(res.content)
        user = User.objects.filter(is_staff = False)
        self.assertEqual(res_data , LeaderBoardSerializer(user , many = True).data)
        self.assertEqual(res.status_code , 200)

    # Get Question
    def test_get_question_withoutQuery(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.questions_url)
        res_data = json.loads(res.content)
        self.assertEqual(res.status_code , 400)
    
    def test_get_question_withQuery(self):
        self.client.force_authenticate(user =self.user)
        data = {"world": "1" ,"section" : "1" ,"role": "testing role","questionLevel": 1}
        res = self.client.generic(method="GET", path= self.questions_url, data=json.dumps(data), content_type='application/json')
        res_data = json.loads(res.content)

        world = World.objects.get(name = '1')
        section = Section.objects.get(name = '1')
        questions = Questions_teacher.objects.filter(worldID = world , sectionID  = section , role = 'testing role', questionLevel = 1 )   
      
        self.assertEqual(res.status_code , 200)
        self.assertEqual(res_data , QuestionTeacherSerializer(questions , many = True).data)

    # Post Question Answer
    def test_post_questionAns(self):
        self.client.force_authenticate(user = self.user)
        data = {'world': self.question.worldID.name ,'section':self.question.sectionID.name,
        'questionID': self.question.id, 'studentID':self.user.id,  'studentAnswer': '2',  'isAnsweredCorrect': True } 
        res = self.client.post(self.questions_url , data = data , format='json')
        res_data = json.loads(res.content)

        self.assertEqual(res_data , {'pass':True} )
        self.assertEqual(res.status_code , 201)

    def test_post_questionAns_Without_Data(self):
        self.client.force_authenticate(user = self.user)
        res = self.client.post(self.questions_url)
        res_data = json.loads(res.content)

        self.assertEqual(res_data , {'pass':False})
        self.assertEqual(res.status_code, 400)

    # Student Post new Question
    def test_post_create_StudentQuestion_Without_Data(self):
        self.client.force_authenticate(user = self.user)
        res = self.client.post(self.create_questions_url)
        res_data = json.loads(res.content)
        
        self.assertEqual(res_data , {'submitted':False})
        self.assertEqual(res.status_code , 400)
    
    def test_post_create_StudentQuestion_With_Data(self):
        self.client.force_authenticate(user = self.user)
        data ={ 'Proposer': 'student@gmail.com' , 'isMCQ': True,  'questionBody': '10*10 = ?', 
        'questionAns'  : [{  'questionText': '1', 'isCorrect' : False  },  { 'questionText': '10', 'isCorrect' : False },
        {'questionText': '10', 'isCorrect' : False  },  {'questionText': '100', 'isCorrect' : True }]} 
        res = self.client.post(self.create_questions_url , data = data ,format='json')
        res_data = json.loads(res.content)

        self.assertEqual(res_data , {'submitted':True})
        self.assertEqual(res.status_code , 201)

    def test_game_summary(self):
        self.client.force_authenticate(user = self.user)
        data ={'email' : self.user.email}
        res = self.client.generic(method="GET", path= self.game_summary_url, data=json.dumps(data), content_type='application/json')
        res_data = json.loads(res.content)
        student = User.objects.get(email = self.user.email)
        self.assertEqual( res_data , gameSummarySerializer(student).data)
        self.assertEqual(res.status_code , 200)
    
    def test_game_summary_with_no_input(self): 
        self.client.force_authenticate(user = self.user)
        res = self.client.generic(method="GET", path= self.game_summary_url, content_type='application/json')
        res_data = json.loads(res.content)
        self.assertEqual( res_data , {'Error Message': 'record not found'})
        self.assertEqual(res.status_code , 400)