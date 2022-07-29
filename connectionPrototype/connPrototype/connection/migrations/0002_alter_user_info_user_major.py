# Generated by Django 4.0.6 on 2022-07-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_major',
            field=models.CharField(choices=[('Math', 'Mathematics'), ('CS', 'Computer Science'), ('Bio', 'Biology'), ('Japn', 'Japanese Studies'), ('Chem', 'Chemistry'), ('SE', 'Structural Engineering')], max_length=25),
        ),
    ]