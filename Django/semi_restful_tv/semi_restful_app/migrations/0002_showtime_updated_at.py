# Generated by Django 2.2.4 on 2020-12-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtime',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
