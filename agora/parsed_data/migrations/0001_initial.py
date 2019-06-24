# Generated by Django 2.2.2 on 2019-06-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_num_num', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_num', models.CharField(max_length=200)),
                ('raw_name', models.CharField(max_length=200)),
                ('raw_attribue', models.CharField(max_length=200)),
                ('raw_condition', models.CharField(max_length=200)),
                ('raw_department', models.CharField(max_length=200)),
                ('raw_status', models.CharField(max_length=200)),
            ],
        ),
    ]