# Generated by Django 3.1.5 on 2021-07-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_partner_indef'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='GoogleDisk',
            field=models.URLField(verbose_name='Посилання на гугл диск'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='fb',
            field=models.URLField(blank=True, verbose_name='Посилання на Facebook'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='linkedIn',
            field=models.URLField(blank=True, verbose_name='Посилання на linkedIn'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='personal_page',
            field=models.URLField(blank=True, verbose_name='Посилання на персональну сторінку'),
        ),
    ]
