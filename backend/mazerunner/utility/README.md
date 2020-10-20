# Database script
## Load user, world, section, questions from our datasets with csv format
### Testing script
``` python
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

                if(question.questionLevel !='3'):
                    Questions_answer.objects.create(questionID = question ,questionText= row[6] ,isCorrect = False)
                    Questions_answer.objects.create(questionID = question ,questionText= row[7] ,isCorrect = False)
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
```



# Load & Performance Testing using Locust

## Introduction
LocustIO, an open source tool written in python, is used for load testing of web applications. It's used with web UI to view the test results.
Locust emulates the users perfrom the testing tasks on the application and measure the performance of the number of requests for different tasks and analysis the success and failure of those requests.
In our testings, we have 6 test cases:
* get_student_list
* get_leaderboard
* get_question
* get_gameSummary
* post_question_ans
* post_question_create

## How to Run locust
* 1.Open new cmd and change directory to locust file
* 2.Enter command - "locust -f locust.py"
* 3.Open Web browser and enter the site  - "http://localhost:8089/"
* 4.Enter the number of user and the spawn rate
* 4.Enter the number of `user` and the `spawn rate`


## Testing script
``` python
from locust import TaskSet, task, between , HttpUser
import json

""" user authentication """
class UserBehaviour(TaskSet):
    header = {"authorization" : "Token bdfeedd723094892a05ab8bafb422c70ec00ae43"}
    student = {"email":"jy@gmail.com", "password":"password"}
    
    @task
    def login(self):
        res = self.client.post("/api/login/", json=self.student)
        print(res.content)
        res_data = json.loads(res.content)
        self.header = {"authorization" : "Token " +res_data['token']}
    
    @task
    def get_student_list(self):
        res = self.client.get("/api/students", headers=self.header)
        print(res.content)
        
    @task
    def get_leaderboard(self):
        res = self.client.get("/api/students/leaderboard", headers=self.header)
        print(res.content)

    @task
    def get_question(self):
        data = {'world': 'World1', 'section': '1', 'role': '2', 'questionLevel': 1}
        res = self.client.get("/api/questions",headers=self.header, json=data)
        print(res.content)

    @task
    def get_gameSummary(self):
        data = {'email' : 'jy@gmail.com'}
        res = self.client.get("/api/gameSummary" , headers = self.header , json=data)
        print(res.content)
    
    @task
    def post_question_ans(self):
        data = {'world': 'World1','section':'1',
        'questionID': 1, 'studentID': 1,  'studentAnswer': '2',  'isAnsweredCorrect': True }  
        res = self.client.post("/api/questions",headers = self.header , json = data)
        print(res.content)

    @task
    def post_question_create(self):
        data ={ 'Proposer': self.student['email'] , 'isMCQ': True,  'questionBody': '10*10 = ?', 
        'questionAns'  : [
            {  'questionText': '1', 'isCorrect' : False  }, 
            { 'questionText': '10', 'isCorrect' : False },
            {'questionText': '10', 'isCorrect' : False  },  {'questionText': '100', 'isCorrect' : True }]} 
        res = self.client.post("/api/questions/create", headers = self.header , json = data)
        print(res.content)

class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 5000
    max_wait = 15000
    host = "http://127.0.0.1:8000"
```
## Testing results
* Columns represents in the results:
1. `Type of requests` - related to each task to be simulated.
2. `Name` - Name of the task/request.
3. `Number of requests` - Total number of requests for a task.
4. `Number of failures` - Total number of failed requests.
5. The `median, average, max and min of requests` in milliseconds.
6. `Content size` - Size of requests data.
7. `Request per second`.

The detailed rsults are saved as *.html in our `test` folder. The below two pictures are used to support our observations.
* 1. Simulate `700 users` with `spawned rate 70` users per second.

![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/blob/master/backend/mazerunner/tests/700users_70.png)

* 2. Simulate `800 users` with `spawned rate 80` users per second.

![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/blob/master/backend/mazerunner/tests/800users_80.png)

## Observations
### Load testings
* To test the load caopability of our server, we gradually increased the spawned rate from 10 to 100. Compare the result 1 and result 2, we can find that our server can response the requests from 70 users per second at most. Once the spawned rate increases to 80, our server will crash. 
* Most of the failures are at creating questions.
### Performance testings
* When the spawned rate is below 80 users per second, 99 percentage of requests are reponsed with 1 second.
* Among the 6 testing cases, `login` requests need more time to receive the reponse from server because of the authenticating process. 



