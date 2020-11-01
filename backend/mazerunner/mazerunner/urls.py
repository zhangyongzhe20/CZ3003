"""mazerunner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('', admin.site.urls),
    path('nested_admin', include('nested_admin.urls')),
    path('', include('api.urls')),
    path('stats', TemplateView.as_view(template_name="post_assignment.html")),
    path('openapi/', get_schema_view(
        title="MazeRunner",
        description="Generated API documentation by Swagger"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),


]

admin.site.site_header = 'Mazerunner Administration'
admin.site.index_title = 'Teacher Administration Site '