# Generated by Django 4.2.6 on 2023-10-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id_course', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_course', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('objects_course', models.CharField(max_length=255)),
                ('gv', models.CharField(max_length=50)),
            ],
        ),
    ]