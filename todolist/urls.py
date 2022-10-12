from django.urls import path
from todolist.views import todolist, create_task, register, login_user, logout_user, refresh, delete, show_json

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login-user/', login_user, name='login_user'),
    path('logout-user/', logout_user, name='logout_user'),
    path('refresh/<str:id>/', refresh, name="refresh"),
    path('delete/<str:id>/', delete, name="delete"),
    path('json/', show_json, name='show_json'),
]