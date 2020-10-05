"""Whitebox testing implemented with Django unittest for our components: User, Question, gameHistory and RESTful API"""
""" All code in setUp will be run once before each test case """

"""Django libs used in the test cases"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime

""" import our components """
from users.models import User
from questions.models import Questions_teacher, Questions_answer, World, Section
from gameHistory.models import questionHistory


class ModelTests(TestCase):
    """ setup starts """
    def setUp(self):
        """ Create a student account """
        self.student = get_user_model().objects.create_user(
            email = 'student1@mail.com',
            password = 'student1',
            name = 'student1',
            distanceToNPC = 0,
            overallScore = 0,
            containBonus = False
            )

        """ Create a teacher account """
        self.teacher = get_user_model().objects.create_superuser(
            email = 'teacher1@mail.com',
            password = 'teacher1',
        )

        """ Create a World & Section BEFORE create a question """
        self.world1 = World.objects.create(name="1")
        self.section1 = Section.objects.create(name="1")

        """ Create a teacher question """
        self.question1 = Questions_teacher.objects.create(
            questionBody="What's HTML used for?",
            isMCQ=False,
            worldID=self.world1,
            sectionID=self.section1,
            role="frontend",
            questionLevel=1)   

        """ Create an answer for a question """
        self.answer1 = Questions_answer.objects.create(
            questionID = self.question1,
            questionText = "Web development",
            isCorrect = True
        )

        """ Create a question played history """
        self.questionRecord = questionHistory.objects.create(
            worldID=self.world1, 
            sectionID=self.section1, 
            questionID=self.question1,
            studentID=self.student, 
            isAnsweredCorrect=True, 
            studentAnswer='test')  
    """ setup ends """

    """ test cases start """
    def test_create_student(self):
        """ test the student is created """
        student = get_user_model().objects.get(email='student1@mail.com')
        """ check all atributes of student are correct """
        self.assertEqual(student.name, 'student1')
        self.assertTrue(student.check_password('student1'))
        self.assertEqual(student.distanceToNPC, 0)
        self.assertEqual(student.overallScore, 0)
        self.assertEqual(student.containBonus, False)

    def test_create_teacher(self):
        """ test a teacher account is created """
        teacher = get_user_model().objects.get(email = 'teacher1@mail.com')
        """ check all atributes of teacher are correct """
        self.assertTrue(teacher.check_password('teacher1'))
        self.assertEqual(teacher.is_staff, True)

    def test_create_teacherQuestion(self):
        """ test a teacher question is created """
        question = Questions_teacher.objects.get(worldID = self.world1)
        """ check all atributes of teacher questions are correct """
        self.assertEqual(question.questionBody, "What's HTML used for?")
        self.assertEqual(question.isMCQ, False)
        self.assertEqual(question.role, "frontend")
        self.assertEqual(question.questionLevel, 1)

    def test_create_questionAnswer(self):
        """ test an answer of a teacher question is created """
        answer = Questions_answer.objects.get(questionID = self.question1)
        """ check all atributes of an answer a question are correct """
        self.assertEqual(answer.questionText, "Web development")
        self.assertEqual(answer.isCorrect, True)

    def test_create_game_history(self):
        """ test a record of question played by student is created """
        question_record = questionHistory.objects.get(questionID = self.question1)
        """ check all atributes of an answer a question are correct """
        self.assertEqual(question_record.worldID, self.world1)
        self.assertEqual(question_record.sectionID, self.section1)
        self.assertEqual(question_record.studentID, self.student)
        self.assertEqual(question_record.isAnsweredCorrect, True)
        self.assertEqual(question_record.studentAnswer, "test")

    """ test cases end """