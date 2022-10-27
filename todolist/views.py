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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

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

#--------------------------------------------VIEWS--------------------------------------------#
@login_required(login_url='/todolist/login-user/')
def show_todolist(request):
    if request.user.is_authenticated:
        user_name = request.user.username 
        data_tasklist = Task.objects.filter(user= request.user)
        context = {'todolist': data_tasklist, 
                    'username': user_name,
        }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login-user/') # login first before doing this
def create_task(request):
    user_name = User.objects.get(username=request.user)    
    form = TaskForm()
    new_task = None
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'create-task.html', context)

#---------------------------------AJAX Implementation-----------------------------------------#
def create_task_ajax(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        date = datetime.datetime.now()
        is_finished = False
        item = Task(title=title, description=description, user=user, date=date, is_finished=is_finished)
        item.save()
        return JsonResponse({"Message": "Task Success"},status=200)

def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

@csrf_exempt
def refresh(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not(task.is_finished)
    task.save(update_fields = ['is_finished'])
    return JsonResponse({"Message": "Task Updated"},status=200)

@csrf_exempt
def delete(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return JsonResponse({"Message": "Task Deleted"},status=200)
#---------------------------------------------------------------------------------------------#