# Generated by Django 5.1 on 2024-09-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('cid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
                ('seats', models.IntegerField()),
                ('roomno', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]