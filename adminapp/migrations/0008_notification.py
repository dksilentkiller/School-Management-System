# Generated by Django 5.1 on 2024-09-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('doc', models.FileField(upload_to='')),
                ('created_date', models.DateField()),
            ],
        ),
    ]
