# Generated by Django 5.0.4 on 2024-04-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0021_alter_group_alloted_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='has_wicketkeeper',
            field=models.BooleanField(default=False),
        ),
    ]