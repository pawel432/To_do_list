import datetime
import logging
from typing import List

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from appCalendar.models import Task
from toDoList.forms import TaskForm

# Create your views here.

logger = logging.getLogger(__name__)


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
            return redirect('user_tasks_page', month=mainPageMonth, year=mainPageYear, filter='default')
        elif templateName == "dayTasks.html":
            return redirect('day_tasks', month=mainPageMonth, year=mainPageYear, day=mainPageDay)


@login_required
def deleteTask(request, taskId, mainPageMonth, mainPageYear, mainPageDay=None):
    Task.objects.get(id=taskId).delete()
    if mainPageDay is not None:
        return redirect('day_tasks', month=mainPageMonth, year=mainPageYear, day=mainPageDay)
    else:
        return redirect('user_tasks_page', month=mainPageMonth, year=mainPageYear, filter='default')


# def changeMonthFormat(monthList: List, monthNumber: int, year: int):
#     for week in monthList:
#         for day in range(0, len(week)):
#             oldDayVar = week[day]
#             week[day] = [oldDayVar, monthNumber, year]


def changeMonthFormat(monthList: List, monthNumber: int, year: int):
    tasks = False
    for week in monthList:
        for day in range(0, len(week)):
            oldDayVar = week[day]
            week[day] = [oldDayVar, monthNumber, year, tasks]


def areTasksExist(monthList: List):
    for week in monthList:
        for day in range(0, len(week)):
            logger.info(day)
            tasksQuerySet = Task.objects.filter(date=datetime.date(week[day][2], week[day][1], week[day][0]))
            if len(tasksQuerySet) > 0:
                week[day][3] = True


def ifTaskDoesNotExist(mainPageMonth, mainPageYear, mainPageDay=None):
    if mainPageDay is not None:
        return redirect('day_tasks', month=mainPageMonth, year=mainPageYear, day=mainPageDay)
    else:
        return redirect('user_tasks_page', month=mainPageMonth, year=mainPageYear, filter='default')
