# Generated by Django 2.2.7 on 2019-12-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_projects_imagegalery'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataforgalery',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
