# Generated by Django 3.2.4 on 2021-06-16 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updeted_on',
            new_name='updated_on',
        ),
    ]
