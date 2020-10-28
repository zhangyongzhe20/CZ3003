""" Using Locust lib for the load & performance test """
from locust import TaskSet, task, between , HttpUser
import json

'''List of task to be included for stress and peformance test '''
class UserBehaviour(TaskSet):
    """ user authentication """
    header = {"authorization" : "Token 45b484f113cf89bf94dbf11062f28c0478d846a2"}
    student = {"email":"jy@gmail.com", "password":"password"}
    

    ''' the weight ratio of task '''
    ''' post_question_ans(every question)  : post_query_for_question_list(every section) : get_leaderboard (depends): get_student_list (same as get_leaderboard)  
        : post_question_create (depends): login (one time per user) '''
    ''' 10 : 4 : 3 : 3 : 2 : 1'''
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


    # '''function to call api to get game summary based on student email for stress and peformance test '''
    # @task
    # def get_gameSummary(self):
    #     data = {'email' : 'jy@gmail.com'}
    #     res = self.client.get("/api/gameSummary" , headers = self.header , json=data)
    #     print(res.content)
    

    '''function to call api to create question history based on question and student for stress and peformance test '''
    @task(10)
    def post_question_ans(self):
        data = {'world': '1','section':'1',
        'questionID': 1, 'studentID': 1,  'studentAnswer': '2',  'isAnsweredCorrect': True }  
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
''' driver program '''
class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 5000
    max_wait = 15000
    host = "http://127.0.0.1:8000"