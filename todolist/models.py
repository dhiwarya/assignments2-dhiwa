import datetime
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=250)
    description = models.TextField()
