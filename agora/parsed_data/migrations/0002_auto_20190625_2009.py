# Generated by Django 2.2.2 on 2019-06-25 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pa_board',
            name='laws',
        ),
        migrations.RemoveField(
            model_name='pa_board2',
            name='laws',
        ),
        migrations.RemoveField(
            model_name='par_board',
            name='regu',
        ),
        migrations.RemoveField(
            model_name='par_board2',
            name='regu',
        ),
        migrations.RemoveField(
            model_name='pg_board',
            name='raws',
        ),
        migrations.RemoveField(
            model_name='pg_board2',
            name='raws',
        ),
    ]