# Generated by Django 4.1 on 2022-09-29 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0002_rename_thetodolist_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]