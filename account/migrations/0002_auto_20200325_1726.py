# Generated by Django 2.2.2 on 2020-03-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
