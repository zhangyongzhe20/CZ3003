# Generated by Django 2.2 on 2020-09-08 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gameHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='world',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='questionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('isAnsweredCorrect', models.BooleanField(default=False)),
                ('studentAnswer', models.CharField(default='1', max_length=30)),
                ('gameHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameHistory.gameHistory')),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Questions_teacher')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
        migrations.AddField(
            model_name='gamehistory',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameHistory.section'),
        ),
        migrations.AddField(
            model_name='gamehistory',
            name='world',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameHistory.world'),
        ),
    ]
