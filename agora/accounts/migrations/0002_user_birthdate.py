# Generated by Django 2.2.2 on 2019-06-21 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]