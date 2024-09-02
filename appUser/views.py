from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect

from appUser.models import CustomUser
from appUser.renderViews import signErrorRender, startPageRender
from toDoList.forms import SignInForm, SignUpForm


# Create your views here.


def signUp(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['mail']
        username = form.cleaned_data['username']
        nick = form.cleaned_data['nick']
        password = form.cleaned_data['password']
        repeatPassword = form.cleaned_data['repeatPassword']
        if password == repeatPassword:
            try:
                CustomUser.objects.get(username=username)
                return signErrorRender(request, "signUp.html", "A user with this username already exists.")
            except CustomUser.DoesNotExist:
                CustomUser.objects.create_user(email=email, username=username, first_name=nick, password=password)
                return authorizeUser(request, username, password)
        else:
            return signErrorRender(request, "signUp.html", "Passwords are not the same.")
    else:
        return signErrorRender(request, "signUp.html", "Validation failed.")


def signIn(request):
    form = SignInForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            CustomUser.objects.get(username=username)
            return authorizeUser(request, username, password)
        except CustomUser.DoesNotExist:
            return signErrorRender(request, "signIn.html", "A user with this username does not exist.")
    else:
        return signErrorRender(request, "signIn.html", "Validation failed.")


def authorizeUser(request, username, password):
    authorizedUser = authenticate(request, username=username, password=password)
    if authorizedUser is not None:
        login(request, authorizedUser)
        return redirect('main_page')
    else:
        return signErrorRender(request, "signIn.html", "Invalid password.")


def logOut(request):
    user = request.CustomUser
    if user.is_authenticated:
        logOut(request)
        return startPageRender(request)
    else:
        return HttpResponse("The user is unauthorized", status=401)
