# Generated by Django 4.0.6 on 2022-08-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_karma',
            field=models.IntegerField(default=0),
        ),
    ]