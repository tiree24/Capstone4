# Generated by Django 3.2 on 2021-04-18 07:39

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='settings.MEDIA_URL')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('search_str', models.TextField(max_length=50)),
                ('created_by', models.ManyToManyField(related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
