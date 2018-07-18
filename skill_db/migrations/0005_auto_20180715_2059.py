# Generated by Django 2.0.7 on 2018-07-15 17:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('skill_db', '0004_auto_20180715_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_student', models.BooleanField(default=False)),
                ('is_staffy', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='staff',
            name='is_staffy',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staffy',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_student',
        ),
    ]
