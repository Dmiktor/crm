# Generated by Django 3.1.5 on 2021-07-15 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0007_auto_20210714_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workersteam',
            old_name='title',
            new_name='titleW',
        ),
        migrations.AlterField(
            model_name='project',
            name='main',
            field=models.TextField(blank=True, max_length=600, verbose_name='Сутність та стислий опис'),
        ),
    ]
