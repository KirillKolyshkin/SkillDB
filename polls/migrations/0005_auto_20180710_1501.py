# Generated by Django 2.0.7 on 2018-07-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_skills_skill_lvl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_lvl',
            field=models.CharField(max_length=30),
        ),
    ]
