from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from appCalendar.models import Task
from toDoList.forms import TaskForm


# Create your views here.


@login_required
def newTask(request, mainPageMonth, mainPageDay, mainPageYear):
    form = TaskForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        Task.objects.create(user=request.CustomUser, title=title, date=date, time=time)
        return redirect('day_tasks', month=mainPageMonth, day=mainPageDay, year=mainPageYear)


@login_required
def editTask(request, taskId, mainPageMonth, mainPageYear, templateName, mainPageDay=None):
    form = TaskForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        task = Task.objects.get(id=taskId)
        task.title = title
        task.date = date
        task.time = time
        task.save()
        if templateName == "userTasksPage.html":
            return redirect('user_tasks_page', month=mainPageMonth, year=mainPageYear)
        elif templateName == "dayTasks.html":
            return redirect('day_tasks', month=mainPageMonth, year=mainPageYear, day=mainPageDay)


@login_required
def deleteTask(request, taskId, mainPageMonth, mainPageYear, mainPageDay=None):
    Task.objects.get(id=taskId).delete()
    if mainPageDay is not None:
        return redirect('day_tasks', month=mainPageMonth, year=mainPageYear, day=mainPageDay)
    else:
        return redirect('user_tasks_page', month=mainPageMonth, year=mainPageYear)
