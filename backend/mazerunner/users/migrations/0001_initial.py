# Generated by Django 2.2 on 2020-09-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('distanceToNPC', models.IntegerField(default=0)),
                ('overallScore', models.IntegerField(default=0)),
                ('Ranking', models.IntegerField(default=0)),
                ('containBonus', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
