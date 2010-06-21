from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

from utils import render
from forms import LoginForm

@render('home.html')
def home(request):
    my_name = "seb"
    return locals()

@render('login_form.html')
def login_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return locals()

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
