# Generated by Django 2.2.7 on 2019-11-24 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20191124_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
