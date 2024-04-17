# Generated by Django 5.0.4 on 2024-04-17 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0018_remove_group_alloted_team_group'),
        ('Teams', '0004_remove_team_time_taken_team_points_scored_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='alloted_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='Teams.team'),
        ),
    ]