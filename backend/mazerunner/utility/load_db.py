import sys
import os
import django
import csv

os.chdir("../")
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'mazerunner.settings'
django.setup()

from users.models import User
from questions.models import World
from questions.models import Section
from questions.models import Questions_teacher
from questions.models import Questions_answer

''' function to create users and load into the database'''
def load_users_data(): 
    User.objects.create_user(email = 'John@mail.com',password = 'password',name = 'John',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Marry@mail.com',password = 'password',name = 'Mary',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'James@mail.com',password = 'password',name = 'James',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Jayce@mail.com',password = 'password',name = 'Jayce',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Annie@mail.com',password = 'password',name = 'Annie',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Ian@mail.com',password = 'password',name = 'Ian',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Ethan@mail.com',password = 'password',name = 'Ethan',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Jolene@mail.com',password = 'password',name = 'Jolene',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Sandy@mail.com',password = 'password',name = 'Sandy',distanceToNPC = 0,overallScore = 0,containBonus = False),
    User.objects.create_user(email = 'Sarah@mail.com',password = 'password',name = 'Sarah',distanceToNPC = 0,overallScore = 0,containBonus = False),

''' function to create worlds and load into the database'''
def load_worlds_data():
    World.objects.create(name = '1' , description='World 1')
    World.objects.create(name = '2' , description='World 2')
    World.objects.create(name = '3' , description='World 3')
    World.objects.create(name = '4' , description='World 4')
    World.objects.create(name = '5' , description='World 5')

''' function to create sections and load into the database'''
def load_sections_data():
    Section.objects.create(name = '1' , description = 'Section 1')
    Section.objects.create(name = '2' , description = 'Section 2')
    Section.objects.create(name = '3' , description = 'Section 3')
    Section.objects.create(name = '4' , description = 'Section 4')
    Section.objects.create(name = '5' , description = 'Section 5')

''' function to create questions and load into the database'''
def load_questions_data():
    with open(os.path.join(os.getcwd(),"" "utility","questions.csv")) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != "world":
                world, created = World.objects.get_or_create(name = row[0])
                section, created = Section.objects.get_or_create(name = row[1])
                question = Questions_teacher.objects.create(worldID= world , sectionID = section , role = row[2] ,
                questionLevel = row[3] , questionBody = row[4])
                Questions_answer.objects.create(questionID = question , questionText =row[5] , isCorrect = True)

                if(question.questionLevel != 3):
                    Questions_answer.objects.create(questionID = question ,questionText= row[6] ,isCorrect = False)
                    Questions_answer.objects.create(questionID = question ,questionText= row[7] ,isCorrect = False)
                    Questions_answer.objects.create(questionID = question , questionText=row[8] ,isCorrect = False)

def load_db(): 
    load_users_data()
    load_worlds_data()
    load_sections_data()
    load_questions_data()

if __name__ == "__main__":
    load_db()