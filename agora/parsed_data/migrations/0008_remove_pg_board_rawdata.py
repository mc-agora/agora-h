# Generated by Django 2.2.2 on 2019-06-26 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0007_auto_20190626_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pg_board',
            name='rawdata',
        ),
    ]
