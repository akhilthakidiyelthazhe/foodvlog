# Generated by Django 2.2 on 2021-12-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
