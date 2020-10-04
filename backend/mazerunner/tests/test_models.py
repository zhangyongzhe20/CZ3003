# from django.test import TestCase
# from questions.models import Questions_teacher, Questions_answer
# from users.models import Student
# from gameHistory.models import gameHistory,questionHistory, Section, World
# from datetime import datetime


# class ModelTests(TestCase):

#     def test_create_gameHistory(self):
#         """Create a world first"""
#         name = "world1"
#         world = World.objects.create(name = name)
#         self.assertEqual(world.name, name)

#         """Create a section first"""
#         name = "section1"
#         section = Section.objects.create(name = name)
#         self.assertEqual(section.name, name)

#         """Create a gameHistory first"""
#         game = gameHistory.objects.create(world = world, section= section)


#         """Create a student first"""
#         account = "yongzhe"
#         password = "user"
#         name = "zyz"
#         distanceToNPC=0
#         overallScore=0
#         Ranking=0
#         containBonus=False
#         role= "none"

#         player = Student.objects.create(
#             account = account,
#             password = password,
#             name = name,
#             distanceToNPC = distanceToNPC,
#             overallScore = overallScore,
#             Ranking = Ranking,
#             containBonus = containBonus,
#             role = role
#         )
#         self.assertEqual(player.account, account)

#         """Create a question first"""
#         questionBody = "what is w?"
#         isMCQ = False
#         world = "world2"
#         section = "section2"
#         role = "software engineer"
#         questionLevel = 1

#         Tquestion = Questions_teacher.objects.create(
#             questionBody = questionBody,
#             isMCQ = isMCQ,
#             world = world,
#             section = section,
#             role = role,
#             questionLevel = questionLevel
#         )
#         self.assertEqual(Tquestion.questionBody, questionBody)

#         """test of creating a game history"""
#         timestamp = datetime.now()
#         isAnsweredCorrect = False
#         studentAnswer = "2"

#         question_History = questionHistory.objects.create(
#             gameHistory = game,
#             questionID = Tquestion,
#             studentID = player,
#             timestamp = timestamp,
#             isAnsweredCorrect = isAnsweredCorrect,
#             studentAnswer = studentAnswer
#         )
#         ## Definte failed
#         # self.assertEqual(question_History.timestamp, timestamp)
#         ## Just some of cases, not completed
#         self.assertEqual(question_History.studentAnswer, studentAnswer)
#         self.assertEqual(question_History.gameHistory, game)
#         self.assertEqual(question_History.gameHistory.world.name, "world1")




#     def test_create_player(self):
#         """Test of creating player"""
#         account = "yongzhe"
#         password = "user"
#         name = "zyz"
#         distanceToNPC=0
#         overallScore=0
#         Ranking=0
#         containBonus=False
#         role= "none"

#         player = Student.objects.create(
#             account = account,
#             password = password,
#             name = name,
#             distanceToNPC = distanceToNPC,
#             overallScore = overallScore,
#             Ranking = Ranking,
#             containBonus = containBonus,
#             role = role
#         )

#         self.assertEqual(player.account, account)
#         self.assertEqual(player.password, password)
#         self.assertEqual(player.name, name)
#         self.assertEqual(player.distanceToNPC, distanceToNPC)
#         self.assertEqual(player.overallScore, overallScore)
#         self.assertEqual(player.Ranking, Ranking)
#         self.assertEqual(player.containBonus, containBonus)
#         self.assertEqual(player.role, role)


#     def test_create_Tquestions(self):
#         """Test of creating teacher questions"""
#         questionBody = "what is w?"
#         isMCQ = False
#         world = "world2"
#         section = "section2"
#         role = "software engineer"
#         questionLevel = 1

#         Tquestion = Questions_teacher.objects.create(
#             questionBody = questionBody,
#             isMCQ = isMCQ,
#             world = world,
#             section = section,
#             role = role,
#             questionLevel = questionLevel
#         )

#         self.assertEqual(Tquestion.questionBody, questionBody)
#         self.assertEqual(Tquestion.isMCQ, isMCQ)
#         self.assertEqual(Tquestion.world, world)
#         self.assertEqual(Tquestion.section, section)
#         self.assertEqual(Tquestion.role, role)
#         self.assertEqual(Tquestion.questionLevel, questionLevel)


#     def test_create_questionAnswers(self):
#         """Test of creating answer of questions"""


#         Tquestion = Questions_teacher.objects.create(
#         questionBody = "what is w?",
#         isMCQ = False,
#         world = "world2",
#         section = "section2",
#         role = "software engineer",
#         questionLevel = 1
#         )

#         questionText = "choice1"
#         isCorrect = True
#         ans = Questions_answer.objects.create(
#             questionID = Tquestion,
#             questionText = questionText,
#             isCorrect = isCorrect
#         )

#         self.assertEqual(ans.questionID, Tquestion)
#         self.assertEqual(ans.questionText, questionText)
#         self.assertEqual(ans.isCorrect, isCorrect)
    

