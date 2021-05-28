# Generated by Django 3.1.5 on 2021-05-18 05:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0005_auto_20210514_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipientServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='personal_page',
            field=models.URLField(blank=True, default='#', verbose_name='Посилання на персональну сторінку'),
        ),
        migrations.AlterField(
            model_name='action',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник"),
        ),
        migrations.AlterField(
            model_name='action',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logic.project', verbose_name="Пов'язаний Проєкт"),
        ),
        migrations.AlterField(
            model_name='action',
            name='rel_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Пов'язаний менеджер"),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectTeams',
            field=models.ManyToManyField(to='logic.WorkersTeam', verbose_name="Пов'язана проєктна команда"),
        ),
        migrations.AlterField(
            model_name='workerprofile',
            name='partner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник"),
        ),
        migrations.AlterField(
            model_name='workersteam',
            name='workers',
            field=models.ManyToManyField(to='logic.WorkerProfile', verbose_name="Пов'язані розробники"),
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник")),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Назва сервісу')),
                ('full', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Вартість у грн.')),
                ('main', ckeditor.fields.RichTextField(blank=True, max_length=250, verbose_name='Тема')),
                ('terms', ckeditor.fields.RichTextField(blank=True, max_length=250, verbose_name='Умови надання')),
                ('target', ckeditor.fields.RichTextField(blank=True, max_length=600, verbose_name='Цільова аудиторія')),
                ('category', models.CharField(choices=[('eco', 'Екологія'), ('bio', 'Біотехнології'), ('mat', 'Матеріалознавство'), ('enr', 'Енергія'), ('all', 'Усі')], default='all', max_length=3, verbose_name='Цільова тематика')),
                ('recipient_of_services', models.ManyToManyField(blank=True, to='logic.RecipientServices', verbose_name='Ожержувачі сервісів')),
                ('rel_projects', models.ManyToManyField(blank=True, to='logic.Project', verbose_name="Пов'язані проєкти")),
                ('service_providers', models.ManyToManyField(to='logic.ServiceProvider', verbose_name='Відровідальні надувачі сервісів')),
            ],
        ),
        migrations.AddField(
            model_name='recipientservices',
            name='partner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник"),
        ),
    ]
