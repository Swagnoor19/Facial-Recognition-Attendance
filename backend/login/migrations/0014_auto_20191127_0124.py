# Generated by Django 2.2.7 on 2019-11-27 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20191124_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='studentPicture',
            field=models.FileField(default=1, upload_to='students/student_pics/'),
        ),
    ]
