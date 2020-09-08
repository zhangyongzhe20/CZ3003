from django.test import TestCase
from questions.models import Questions_teacher, Questions_answer

class ModelTests(TestCase):

    def test_create_Tquestions(self):
        """Test of creating teacher questions"""
        questionBody = "what is w?"
        isMCQ = False
        world = "world2"
        section = "section2"
        role = "software engineer"
        questionLevel = 1

        Tquestion = Questions_teacher.objects.create(
            questionBody = questionBody,
            isMCQ = isMCQ,
            world = world,
            section = section,
            role = role,
            questionLevel = questionLevel
        )

        self.assertEqual(Tquestion.questionBody, questionBody)
        self.assertEqual(Tquestion.isMCQ, isMCQ)
        self.assertEqual(Tquestion.world, world)
        self.assertEqual(Tquestion.section, section)
        self.assertEqual(Tquestion.role, role)
        self.assertEqual(Tquestion.questionLevel, questionLevel)


    def test_create_questionAnswers(self):
        """Test of creating answer of questions"""


        Tquestion = Questions_teacher.objects.create(
        questionBody = "what is w?",
        isMCQ = False,
        world = "world2",
        section = "section2",
        role = "software engineer",
        questionLevel = 1
        )

        questionText = "choice1"
        isCorrect = True
        ans = Questions_answer.objects.create(
            questionID = Tquestion,
            questionText = questionText,
            isCorrect = isCorrect
        )

        self.assertEqual(ans.questionID, Tquestion)
        self.assertEqual(ans.questionText, questionText)
        self.assertEqual(ans.isCorrect, isCorrect)
    


