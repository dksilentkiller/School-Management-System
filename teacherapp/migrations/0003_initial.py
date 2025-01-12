# Generated by Django 5.1 on 2024-09-18 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacherapp', '0002_delete_studymaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sm', models.FileField(upload_to='')),
                ('tclass', models.CharField(max_length=30)),
                ('created_date', models.DateField(default=datetime.date(2024, 9, 18))),
            ],
        ),
    ]
