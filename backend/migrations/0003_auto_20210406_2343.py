# Generated by Django 3.1.7 on 2021-04-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210406_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]