"""
URL configuration for toDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from appCalendar.renderViews import mainPageRender, addTaskPageRender
from appUser.renderViews import startPageRender, signRender, signErrorRender
from appUser.views import signIn, signUp, logOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', startPageRender, name='home'),
    path('signin/', signIn, name='sign_in'),
    path('signup/', signUp, name='sign_up'),
    path('logout/', logOut, name='log_out'),
    path('sign/<str:template>/', signRender, name='sign_render'),
    path('signerror/<str:template>/', signErrorRender, name='sign_error_render'),
    path('mainpage/', mainPageRender, name='main_page'),
    path('addtaskpage/<int:month>/<int:day>/<int:year>/', addTaskPageRender, name='add_task_page')
]
