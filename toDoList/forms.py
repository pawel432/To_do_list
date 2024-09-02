from django import forms


class SignUpForm(forms.Form):
    mail = forms.EmailField(label='E-mail', max_length=35)
    username = forms.CharField(label='Username', max_length=30)
    nick = forms.CharField(label='Nick', max_length=30)
    password = forms.CharField(label='Password', max_length=35, widget=forms.PasswordInput)
    repeatPassword = forms.CharField(label='Repeat password', max_length=35, widget=forms.PasswordInput)


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=35, widget=forms.PasswordInput)


class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=150)
    date = forms.DateField(label='Date')
    time = forms.TimeField(label='Time')
