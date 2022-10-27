from django.urls import path
from todolist.views import show_todolist, create_task, register, login_user, logout_user, refresh, delete, show_json, create_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login-user/', login_user, name='login_user'),
    path('logout-user/', logout_user, name='logout_user'),
    path('refresh/<str:id>/', refresh, name="refresh"),
    path('delete/<str:id>/', delete, name="delete"),
    path('json/', show_json, name='show_json'),
    path('create/', create_task_ajax, name='create_task_ajax')
]