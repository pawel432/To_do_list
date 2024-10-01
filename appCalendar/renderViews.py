import calendar
import datetime
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from appCalendar.models import Task
from appCalendar.views import ifTaskDoesNotExist, changeMonthFormat, areTasksExist
from toDoList.forms import TaskForm

logger = logging.getLogger(__name__)


@login_required
def mainPageRender(request, next_months: str, month: int, year: int):
    next_months = int(next_months)
    month += next_months
    if month == 13:
        month = 1
        year += 1
    if month == 0:
        month = 12
        year -= 1
    if month == 1:
        previous_month = calendar.monthcalendar(year - 1, 12)
        changeMonthFormat(previous_month, 12, year - 1)
    else:
        previous_month = calendar.monthcalendar(year, month - 1)
        changeMonthFormat(previous_month, month - 1, year)
    if month == 12:
        next_month = calendar.monthcalendar(year + 1, 1)
        changeMonthFormat(next_month, 1, year + 1)
    else:
        next_month = calendar.monthcalendar(year, month + 1)
        changeMonthFormat(next_month, month + 1, year)
    current_month = calendar.monthcalendar(year, month)
    changeMonthFormat(current_month, month, year)

    pre_month_last_week_index = len(previous_month) - 1
    cur_month_last_week_index = len(current_month) - 1

    pre_month_last_week = previous_month[pre_month_last_week_index]
    current_month_first_week = current_month[0]
    current_month_last_week = current_month[cur_month_last_week_index]
    next_month_first_week = next_month[0]

    for i in range(0, 7):
        if current_month_first_week[i][0] == 0:
            current_month_first_week[i][0] = pre_month_last_week[i][0]
            current_month_first_week[i][1] = pre_month_last_week[i][1]
            current_month_first_week[i][2] = pre_month_last_week[i][2]
    current_month[0] = current_month_first_week
    for i in range(0, 7):
        if current_month_last_week[i][0] == 0:
            current_month_last_week[i][0] = next_month_first_week[i][0]
            current_month_last_week[i][1] = next_month_first_week[i][1]
            current_month_last_week[i][2] = next_month_first_week[i][2]
    current_month[cur_month_last_week_index] = current_month_last_week
    areTasksExist(current_month)
    return render(request, 'mainPage.html',
                  {'date': current_month,
                   'month': month, 'year': year, 'currentDate': datetime.datetime.now().date()})


@login_required
def addTaskPageRender(request, month, day, year):
    initial_data = {
        'date': datetime.date(year, month, day)
    }
    form = TaskForm(initial=initial_data)
    return render(request, 'addTaskPage.html',
                  {'user': request.CustomUser, 'year': year,
                   'month': month, 'day': day, 'form': form})


@login_required
def userTasksPageRender(request, month, year, filter):
    if filter == "default":
        tasks = Task.objects.filter(user=request.CustomUser).order_by('date',
                                                                      'time')
    else:
        tasks = Task.objects.filter(user=request.CustomUser, date=datetime.datetime.now().date()).order_by('date',
                                                                                                           'time')
    return render(request, 'userTasksPage.html', {'user': request.CustomUser,
                                                  'tasks': tasks,
                                                  'month': month, 'year': year})


@login_required
def dayTasksRender(request, month, year, day):
    return render(request, 'dayTasks.html', {'user': request.CustomUser,
                                             'tasks': Task.objects.filter(date=datetime.date(year, month, day),
                                                                          user=request.CustomUser).order_by('date',
                                                                                                            'time'),
                                             'month': month, 'year': year, 'day': day})


@login_required
def taskPageRender(request, mainPageMonth, mainPageYear, taskId, mainPageDay=None):
    try:
        task = Task.objects.get(id=taskId)
    except Task.DoesNotExist:
        return ifTaskDoesNotExist(mainPageMonth, mainPageYear, mainPageDay)
    initial_data = {
        'title': task.title,
        'date': datetime.date(task.date.year, task.date.month, task.date.day),
        'time': task.time.strftime("%H:%M")
    }
    form = TaskForm(initial=initial_data)
    if mainPageDay is not None:
        return render(request, 'taskPage.html',
                      {'form': form, 'task': task,
                       'mainPageMonth': mainPageMonth, 'mainPageYear': mainPageYear, 'day': mainPageDay})
    else:
        return render(request, 'taskPage.html',
                      {'form': form, 'task': task,
                       'mainPageMonth': mainPageMonth, 'mainPageYear': mainPageYear})


@login_required
def confirmDeleteRender(request, taskId, mainPageMonth, mainPageYear, mainPageDay=None):
    try:
        task = Task.objects.get(id=taskId)
    except Task.DoesNotExist:
        return ifTaskDoesNotExist(mainPageMonth, mainPageYear, mainPageDay)
    if mainPageDay is not None:
        return render(request, 'confirmDeletePage.html', {'task': task,
                                                          'mainPageMonth': mainPageMonth, 'mainPageYear': mainPageYear,
                                                          'day': mainPageDay})
    else:
        return render(request, 'confirmDeletePage.html', {'task': task,
                                                          'mainPageMonth': mainPageMonth, 'mainPageYear': mainPageYear})
