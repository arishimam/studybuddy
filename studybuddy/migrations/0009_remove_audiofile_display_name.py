# Generated by Django 4.2.7 on 2023-12-04 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0008_alter_audiofile_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofile',
            name='display_name',
        ),
    ]
