# Generated by Django 4.0.6 on 2022-08-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.TextField(default=''),
        ),
    ]
