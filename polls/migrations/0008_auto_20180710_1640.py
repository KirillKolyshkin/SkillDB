# Generated by Django 2.0.7 on 2018-07-10 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180710_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='er_email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='er_password',
            new_name='user_password',
        ),
    ]
