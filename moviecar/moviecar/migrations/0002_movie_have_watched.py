# Generated by Django 3.2.12 on 2022-11-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='have_watched',
            field=models.BooleanField(default=False),
        ),
    ]