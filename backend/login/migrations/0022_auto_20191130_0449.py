# Generated by Django 2.2.7 on 2019-11-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20191130_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='classes', to='login.Students'),
        ),
    ]