# Two ways are provided to set up the backend server
## 1. Running server on local computer
### Requirements
1. Python 3.7
### Steps
1. Create an Python virtual environment and install dependencies
```python
cd ./CZ3003-SSAD/backend
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
2. Run the Django migrations to set up your models:
``` python 
python manage.py makemigrations
python manage.py migrate
```
3. Start a local web server:
``` python
python manage.py runserver
```
4. In your browser, go to http://localhost:8000
5. Press `control+C` to stop the local web server.

## 2. Running Server using Docker
### Reuquirements
1. Docker
2. docker-compose.yml
3. Dockerfile
### Steps
1. Change to the directory contains Dockerfile: `cd backend/deployment`
1. Build a docker image: `docker-compose run app`
2. Run the server: `docker-compose up`
3. In your browser, go to http://localhost:8000
3. Stop the server: `docker stop $(docker ps -aq)`