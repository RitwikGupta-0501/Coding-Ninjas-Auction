# Generated by Django 5.0.4 on 2024-04-20 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0005_team_quiz_attempted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='quiz_attempted',
        ),
    ]