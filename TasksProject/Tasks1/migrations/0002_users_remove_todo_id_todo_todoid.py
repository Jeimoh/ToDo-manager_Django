# Generated by Django 5.0.2 on 2024-02-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstNames', models.CharField(max_length=50)),
                ('LastNames', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('DOB', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='id',
        ),
        migrations.AddField(
            model_name='todo',
            name='ToDoId',
            field=models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
