# Generated by Django 5.1.2 on 2024-10-29 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='projects',
            new_name='project',
        ),
    ]