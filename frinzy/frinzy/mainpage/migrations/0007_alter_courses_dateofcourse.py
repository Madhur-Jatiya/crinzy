# Generated by Django 3.2.3 on 2021-05-23 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_alter_courses_dateofcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='dateofcourse',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 17, 13, 28, 388835)),
        ),
    ]
