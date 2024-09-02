import calendar
import datetime

from django.shortcuts import render

from toDoList.forms import SignInForm, SignUpForm


def startPageRender(request):
    return render(request, 'startPage.html')


def signRender(request, template):
    if template == "signIn.html":
        return render(request, 'signIn.html', {'signInForm': SignInForm()})
    if template == "signUp.html":
        return render(request, 'signUp.html', {'signUpForm': SignUpForm()})


def signErrorRender(request, template, errorName):
    if template == "signIn.html":
        return render(request, 'signIn.html', {'signInForm': SignInForm(), 'error': errorName})
    if template == "signUp.html":
        return render(request, 'signUp.html', {'signUpForm': SignUpForm(), 'error': errorName})
