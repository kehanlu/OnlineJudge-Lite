# Generated by Django 2.0.1 on 2018-01-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Judge', '0007_problem_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]