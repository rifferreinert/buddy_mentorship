# Generated by Django 3.1a1 on 2020-05-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_mentorship', '0008_auto_20200526_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='display_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
