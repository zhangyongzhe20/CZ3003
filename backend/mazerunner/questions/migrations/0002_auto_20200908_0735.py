# Generated by Django 2.2 on 2020-09-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='questionType',
        ),
        migrations.AddField(
            model_name='questions',
            name='isMCQ',
            field=models.BooleanField(default=False),
        ),
    ]
