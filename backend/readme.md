# Django_Backend
 This repo serves the development of backend for CZ3003


## Software requirements:
* `python`: 3.7
* `django`: 2.2


## Technical parts:
### Phase 1:
* `Database`: Django ORM; sqlite； Design model schemas;
* `Logical code`: Try to apply some design patterns such as MVC, dependency injection.  [Link](https://subscription.packtpub.com/book/web_development/9781788831345/1/ch01lvl1sec13/what-is-a-pattern)
* `RESTful API`: rest_framework in django; [Link](https://www.django-rest-framework.org/tutorial/quickstart/)
* `Admin page`: Lightweight dashboard

### Phase 2"
* `Testing`
* `Deployment`: Django in Docker. [Link](https://docs.docker.com/compose/django/)

#Update in the django package
i have modified the root admin template in the following directory 
Directory: CZ3003-SSAD\backend\backend_env\Lib\site-packages\django\contrib\admin\templates\admin
backen_env is my virtual environment 
The changes are the following:

1. i have modified the index.html to add a stats button on it
2. Added a post_assignment.html as a dummy template to be redirected to when clicks on to the stats button (this template can be changed later on)

The two new template can be found in the root directory so you may just directly copy it over and paste it in the directory shown above.

Things to take note when new templates are put in
1. urls.py from mazerunner needs to be changed 
This line is this path('stats', templateview.as_view(template_name="post_assignment.html")),
2. settings.py from mazerunner also needs to be changed 
The location is in Templates code section, this will specify where the template is located at so Django knows where to find.



