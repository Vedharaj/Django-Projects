# Generated by Django 4.2.8 on 2023-12-26 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complted',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='taskname',
        ),
    ]
