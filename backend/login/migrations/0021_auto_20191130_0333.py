# Generated by Django 2.2.7 on 2019-11-30 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20191130_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='course',
        ),
        migrations.AddField(
            model_name='classes',
            name='students',
            field=models.ManyToManyField(related_name='classes', to='login.Students'),
        ),
    ]
