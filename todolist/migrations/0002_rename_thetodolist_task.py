# Generated by Django 4.1 on 2022-09-29 03:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="thetodolist", new_name="Task",),
    ]
