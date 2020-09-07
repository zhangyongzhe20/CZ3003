# Generated by Django 2.2 on 2020-09-07 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionBody', models.CharField(max_length=200)),
                ('questionType', models.CharField(max_length=30)),
                ('Proposer', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questions_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionBody', models.CharField(max_length=200)),
                ('questionType', models.CharField(max_length=30)),
                ('world', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questions_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionBody', models.CharField(max_length=200)),
                ('questionType', models.CharField(max_length=30)),
                ('questionText', models.CharField(max_length=200)),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Questions_teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
