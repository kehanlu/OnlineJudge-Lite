# Generated by Django 2.0.1 on 2018-01-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Judge', '0006_auto_20180102_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='school',
            field=models.CharField(default='臺灣科技大學', max_length=200),
            preserve_default=False,
        ),
    ]