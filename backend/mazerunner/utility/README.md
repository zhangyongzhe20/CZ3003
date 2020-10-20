@@ -1,6 +1,95 @@
## How to Run locust
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
* 1. Simulate 10 users with spawned rate 1 user per second.
![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/blob/master/backend/docs/structure.jpeg)


* 2. Simulate 100 users with spawned rate 10 users per second.
![alt text](https://github.com/FrankLeeeee/CZ3003-SSAD/blob/master/backend/docs/structure.jpeg)

## Observations
As seen in result 1, since the number of users is less, there is no failover. While when the number of requests increased to 100 users with spawned rate 10, we get failure rate 

