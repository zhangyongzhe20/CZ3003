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
```



# Load & Performance Testing using Locust

## Introduction
LocustIO, an open source tool written in python, is used for load testing of web applications. It's used with web UI to view the test results.
Locust emulates the users perfrom the testing tasks on the application and measure the performance of the number of requests for different tasks and analysis the success and failure of those requests.
In our testings, we have 6 test cases:
* post_question_ans(every question)
* post_query_for_question_list(every section)
* get_leaderboard (depends)
* get_student_list (same as get_leaderboard)  
* get_Dashboard 
* post_question_create
* login
## How to Run locust
* 1.Open new cmd and change directory to locust file
* 2.Enter command - "locust -f locust.py"
* 3.Open Web browser and enter the site  - "http://localhost:8089/"
* 4.Enter the number of user and the spawn rate
* 4.Enter the number of `user` and the `spawn rate`


## Testing script with weight
``` python
""" Using Locust lib for the load & performance test """
from locust import TaskSet, task, between , HttpUser
import json

'''List of task to be included for stress and peformance test '''
class UserBehaviour(TaskSet):
    """ user authentication """
    header = {"authorization" : "Token e2c7d5894a539f0c823dadb077fe8db17a237efe"}
    student = {"email":"jy@gmail.com", "password":"password"}
    

    ''' the weight ratio of task '''
    ''' post_question_ans(every question)  : post_query_for_question_list(every section) : get_leaderboard (depends): get_student_list (same as get_leaderboard)  
        : get_Dashboard : post_question_create (depends): login (one time per user) '''
    ''' 10 : 4 : 3 : 3 : 2 : 2 : 1'''
    '''function to call api login for stress and peformance test '''
    @task(1)
    def login(self):
        res = self.client.post("/api/login/", json={"email":"jy@gmail.com", "password":"password"})
        print(res.content)
        res_data = json.loads(res.content)
        self.header = {"authorization" : "Token " +res_data['token']}
    
    '''function to call api get list of students for stress and peformance test '''
    @task(3)
    def get_student_list(self):
        res = self.client.get("/api/students", headers=self.header)
        print(res.content)
    
    '''function to call api get leaderboard datas for stress and peformance test '''
    @task(3)
    def get_leaderboard(self):
        res = self.client.get("/api/students/leaderboard", headers=self.header)
        print(res.content)

    '''function to call api get list of questions based on world , section , role and question level for stress and peformance test '''
    @task(4)
    def post_query_for_question_list(self):
        data = {'world': '1', 'section': '1', 'role': '1', 'questionLevel': 1}
        res = self.client.post("/api/questions",headers=self.header, json=data)
        print(res.content)

    '''function to call api to create question history based on question and student for stress and peformance test '''
    @task(10)
    def post_question_ans(self):
        data = {'world': '1','section':'1',
        'questionID': 1, 'studentID': 1,  'studentAnswer': '2',  'isAnsweredCorrect': True , 'pointGain' : 3 }  
        res = self.client.post("/api/questions/submit",headers = self.header , json = data)
        print(res.content)


    '''function to call api to create question based on student for stress and peformance test '''
    @task(2)
    def post_question_create(self):
        data ={ 'Proposer': self.student['email'] , 'isMCQ': True,  'questionBody': '10*10 = ?', 
        'questionAns'  : [
            {  'questionText': '1', 'isCorrect' : False  }, 
            { 'questionText': '10', 'isCorrect' : False },
            {'questionText': '10', 'isCorrect' : False  },  {'questionText': '100', 'isCorrect' : True }]} 
        res = self.client.post("/api/questions/create", headers = self.header , json = data)
        print(res.content)

    @task(2)
    def get_Dashboard(self):
        res = self.client.get("/dashboard", headers=self.header)
        print(res.content)

''' driver program '''
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

## Result with weighted task
The detailed results are saved as *.html in our `test` folder. The below two pictures are used to support our observations.
* 1. Simulate `400 users` with `spawned rate 40` users per second.

![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/tree/master/backend/mazerunner/utility/results/weight/400_40_w.png)

* 2. Simulate `900 users` with `spawned rate 90` users per second.

![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/tree/master/backend/mazerunner/utility/results/weight/900_90_w.png)

## Result with unweight task
* 1. Simulate `400 users` with `spawned rate 40` users per second.

![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/tree/master/backend/mazerunner/utility/results/without_weight/400_40.png)

* 2. Simulate `900 users` with `spawned rate 90` users per second.

![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/tree/master/backend/mazerunner/utility/results/without_weight/900_90.png)


## Observations
### Load testings
* To test the load caopability of our server, we gradually increased the spawned rate from 40 to 90. Compare the result 1 and result 2, we can find that our server can response the requests from 40 users per second at most with or without weighted task. Once the spawned rate increases from 50 to 90, our server are unable to handle all the request.

* Most of the failures are at creating questions.

### Performance testings
* When the spawned rate is below 40 users per second, 99 percentage of requests are reponsed within 1 second.
* Among the 6 testing cases, `login` requests need more average time to receive the reponse from server because of the authenticating process when the server is able to handle all the request. 



