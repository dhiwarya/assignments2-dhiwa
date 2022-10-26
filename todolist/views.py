import datetime
from django.urls import reverse
from django.core import serializers
from todolist.forms import TaskForm
from django.contrib import messages
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#-----------------------------Authentication/Authorization--------------------------------------#
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login_user')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login_user.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login_user')
#---------------------------------------------------------------------------------------------#

#---------------------------------AJAX Implementation-----------------------------------------#
@login_required(login_url='/todolist/login-user/')
def show_todolist(request):
    data_todolist = Task.objects.all()
    user_todolist = []
    name = request.user.username
    for data in data_todolist:
        if data.user.username == name:
            user_todolist.append(data)
    context = {
        'username': name,
        'user_todolist': user_todolist,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login-user/') # login first before doing this
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form_check = form.save(commit=False)
            form_check.user = request.user
            form_check.save()
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
    
    # when requesting 
    return render(request, 'create_task.html', {'form': form})

def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")
#----------------------------------------------------------------------------------------------#

#-----------------------------------------DELETE/REFRESH---------------------------------------#
@login_required(login_url='/todolist/login-user/') # login first before doing this
def refresh(request, id):
    task = Task.objects.get(user = request.user, pk = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todos')

@login_required(login_url='/todolist/login/') # login first before doing this
def delete(request, id):
    task = Task.objects.get(user = request.user, pk = id)
    task.delete()
    return redirect('todolist:show_todos')
#---------------------------------------------------------------------------------------------#