# Generated by Django 4.2.6 on 2023-10-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id_course',
            field=models.CharField(max_length=999, primary_key=True, serialize=False),
        ),
    ]
