# Generated by Django 4.0.6 on 2022-08-12 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_student_user_karma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_created',
        ),
    ]
