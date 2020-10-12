from locust import TaskSet, task, between , HttpUser
import json


header = {"authorization" : "Token bdfeedd723094892a05ab8bafb422c70ec00ae43"}
class UserBehaviour(TaskSet):
   
    @task
    def login(self):
        res = self.client.post("/api/login/", json={"email":"jy@gmail.com", "password":"password"})
        print(res.content)
        res_data = json.loads(res.content)
        token_string = res_data['token']
    
    @task
    def get_student_list(self):
        res = self.client.get("/api/students", headers=header)
        print(res.content)
        
    @task
    def get_leaderboard(self):
        res = self.client.get("/api/students/leaderboard", headers=header)
        print(res.content)

    @task
    def get_question(self):
        data = {'world': 'World1', 'section': '1', 'role': '2', 'questionLevel': 1}
        res = self.client.get("/api/questions",headers=header, json=data)
        print(res.content)


class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 5000
    max_wait = 15000
    host = "http://127.0.0.1:8000"