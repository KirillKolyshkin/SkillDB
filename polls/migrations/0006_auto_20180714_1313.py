# Generated by Django 2.0.7 on 2018-07-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180712_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporarymodel',
            name='lvl',
            field=models.IntegerField(max_length=1),
        ),
    ]
