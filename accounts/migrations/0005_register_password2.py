# Generated by Django 2.2 on 2021-12-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211207_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]