from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from appCalendar.models import Task
from toDoList.forms import TaskForm


# Create your views here.
def allTasks(request):
    tasks = Task.objects.filter(user=request.CustomUser).order_by('date', 'time')
    return tasks


@login_required
def newTask(request, currentPageMonth, currentPageDay, currentPageYear):
    form = TaskForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        Task.objects.create(user=request.CustomUser, title=title, date=date, time=time)
        return redirect('add_task_page', month=currentPageMonth, day=currentPageDay, year=currentPageYear)
