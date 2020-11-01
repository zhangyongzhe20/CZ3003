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
    User.objects.create_user(email = 'John@e.ntu.edu.sg',password = 'password',name = 'John',overallScore = 50)
    User.objects.create_user(email = 'Marry@e.ntu.edu.sg',password = 'password',name = 'Mary',overallScore = 100)
    User.objects.create_user(email = 'James@e.ntu.edu.sg',password = 'password',name = 'James',overallScore = 250)
    User.objects.create_user(email = 'Jayce@e.ntu.edu.sg',password = 'password',name = 'Jayce',overallScore = 300)
    User.objects.create_user(email = 'Annie@e.ntu.edu.sg',password = 'password',name = 'Annie',overallScore = 211)
    User.objects.create_user(email = 'Ian@e.ntu.edu.sg',password = 'password',name = 'Ian',overallScore = 39)
    User.objects.create_user(email = 'Ethan@e.ntu.edu.sg',password = 'password',name = 'Ethan',overallScore = 80)
    User.objects.create_user(email = 'Jolene@e.ntu.edu.sg',password = 'password',name = 'Jolene',overallScore = 90)
    User.objects.create_user(email = 'Sandy@e.ntu.edu.sg',password = 'password',name = 'Sandy',overallScore = 33)
    User.objects.create_user(email = 'Sarah@e.ntu.edu.sg',password = 'password',name = 'Sarah',overallScore = 34)

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
    with open(os.path.join(os.getcwd(),"" "utility","questions2.csv"),  encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'world':
                world, created = World.objects.get_or_create(name = row[0])
                section, created = Section.objects.get_or_create(name = row[1])

                if row[2] != "all":
                    question = Questions_teacher.objects.create(worldID= world , sectionID = section , role = row[2] ,
                    questionLevel = row[3] , questionBody = row[4])

                    Questions_answer.objects.create(questionID = question , questionText =row[5] , isCorrect = True)

                    if(int(question.questionLevel) == 1):
                        if(row[6] != None and row[6] != ""):
                            Questions_answer.objects.create(questionID = question ,questionText= row[6] ,isCorrect = False)
                        if(row[7] != None and row[7] != ""):
                            Questions_answer.objects.create(questionID = question ,questionText= row[7] ,isCorrect = False)
                        if(row[8] != None and row[8] != ""):
                            Questions_answer.objects.create(questionID = question , questionText=row[8] ,isCorrect = False)

                else :
                    roles = ["project manager","backend","frontend"]

                    for role in roles:
                        question = Questions_teacher.objects.create(worldID= world , sectionID = section , role = role ,
                    questionLevel = row[3] , questionBody = row[4])

                    
                        Questions_answer.objects.create(questionID = question , questionText =row[5] , isCorrect = True)

        
                        if(int(question.questionLevel) == 1):
                        
                            if(row[6] != None and row[6] != ""):
                                Questions_answer.objects.create(questionID = question ,questionText= row[6] ,isCorrect = False)
                        
                            if(row[7] != None and row[7] != ""):              
                                Questions_answer.objects.create(questionID = question ,questionText= row[7] ,isCorrect = False)
                            if(row[8] != None and row[8] != ""):
                                Questions_answer.objects.create(questionID = question , questionText=row[8] ,isCorrect = False)

                    


               

'''loading of data function being called'''
def load_db(): 
    '''load all data '''
    load_users_data()
    load_worlds_data()
    load_sections_data()
    load_questions_data()


''' driver program '''
if __name__ == "__main__":
    load_db()
    print("done")