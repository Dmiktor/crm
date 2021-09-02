# Generated by Django 3.1.5 on 2021-09-01 21:30

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Унікальна Адресса')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('main', models.TextField(blank=True, max_length=600, verbose_name='Короткий текст')),
                ('full', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Повний текст')),
                ('category', models.CharField(choices=[('eco', 'Екологія'), ('bio', 'Біотехнології'), ('mat', 'Матеріалознавство'), ('enr', 'Енергія'), ('all', 'Усі')], default='all', max_length=3, verbose_name='Тематика')),
                ('pub', models.CharField(choices=[('int', 'Внутрішній'), ('ext', 'Зовнішній')], default='int', max_length=3, verbose_name='Публічність')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=30, verbose_name='Прізвище')),
                ('nameEn', models.CharField(blank=True, max_length=30, verbose_name="Ім'я Англійською")),
                ('surnameEn', models.CharField(blank=True, max_length=30, verbose_name='Прізвище Англійською')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Електронна пошта ')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон')),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Телефон доп.')),
                ('GoogleDisk', models.URLField(blank=True, verbose_name='Посилання на гугл диск')),
                ('Telegram', models.CharField(blank=True, max_length=30, verbose_name='Telegram')),
                ('info', models.TextField(blank=True, max_length=600, verbose_name='Інф.')),
                ('adress', models.CharField(blank=True, max_length=70, verbose_name='Адреса')),
                ('notion', models.CharField(blank=True, max_length=30, verbose_name='Notion')),
                ('linkedIn', models.URLField(blank=True, verbose_name='Посилання на linkedIn')),
                ('personal_page', models.URLField(blank=True, verbose_name='Посилання на персональну сторінку')),
                ('skype', models.CharField(blank=True, max_length=30, verbose_name='Skype')),
                ('fb', models.URLField(blank=True, verbose_name='Посилання на Facebook')),
                ('isWorker', models.BooleanField(default=False, verbose_name='Розробник?')),
                ('isPartner', models.BooleanField(default=False, verbose_name='Партнер?')),
                ('isSeviceGiver', models.BooleanField(default=False, verbose_name='Надавач сервісів?')),
                ('isSeviceTaker', models.BooleanField(default=False, verbose_name='Користувач сервісів?')),
                ('isInvestor', models.BooleanField(default=False, verbose_name='Інвестор?')),
                ('isStudent', models.BooleanField(default=False, verbose_name='Студент?')),
                ('indef', models.CharField(editable=False, max_length=10)),
                ('valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Коротка назва розробки')),
                ('main', models.TextField(blank=True, max_length=600, verbose_name='Сутність та стислий опис')),
                ('category', models.CharField(choices=[('eco', 'Екологія'), ('bio', 'Біотехнології'), ('mat', 'Матеріалознавство'), ('enr', 'Енергія'), ('all', 'Усі')], default='all', max_length=3, verbose_name='Галузь')),
                ('projectStage', models.CharField(choices=[('rec', 'Дослідження та експериментальне підтвердження'), ('ttl', 'Технологія, перевірена в лабораторії'), ('pro', 'Наявний прототип'), ('tia', 'Технологія має промислові застосування')], default='rec', max_length=3, verbose_name='Ступінь готовності розробки')),
                ('firstvalid', models.BooleanField(default=False, verbose_name='Перша валідіфікація')),
                ('secondvalid', models.BooleanField(default=False, verbose_name='Проект готовий до фінальноі перевірки')),
                ('finalvalid', models.BooleanField(default=False, verbose_name='Проэкт готовий стати инф карткою')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник")),
                ('partnerTags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Список зацікавивших тегів')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(blank=True, max_length=40, verbose_name='Установа')),
                ('position', models.CharField(blank=True, max_length=30, verbose_name='Посада')),
                ('partner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник")),
            ],
        ),
        migrations.CreateModel(
            name='WorkersTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleW', models.CharField(max_length=60, verbose_name='Назва команди')),
                ('rel_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='logic.partner', verbose_name='Відповідальна за команду особа')),
                ('workers', models.ManyToManyField(to='logic.WorkerProfile', verbose_name="Пов'язані розробники")),
            ],
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
                ('terms', models.TextField(blank=True, max_length=250, verbose_name='Умови надання')),
                ('target', models.TextField(blank=True, max_length=600, verbose_name='Цільова аудиторія')),
                ('category', models.CharField(choices=[('eco', 'Екологія'), ('bio', 'Біотехнології'), ('mat', 'Матеріалознавство'), ('enr', 'Енергія'), ('all', 'Усі')], default='all', max_length=3, verbose_name='Цільова тематика')),
                ('partnerTags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Список тегів сервісу')),
                ('recipient_of_services', models.ManyToManyField(blank=True, to='logic.RecipientServices', verbose_name='Ожержувачі сервісів')),
                ('rel_projects', models.ManyToManyField(blank=True, to='logic.Project', verbose_name="Пов'язані проєкти")),
                ('service_providers', models.ManyToManyField(to='logic.ServiceProvider', verbose_name='Відровідальні надувачі сервісів')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('risk', 'Ризики'), ('busi', 'Бізнес план'), ('objc', 'Об`єкт'), ('loca', 'Локація'), ('bran', 'Галузь'), ('prod', 'Продукт'), ('team', 'Команда'), ('inco', 'Рентабельність'), ('fins', 'Фінансування'), ('pers', 'Обслуговуючий персонал'), ('term', 'Вимоги'), ('time', 'Час розгортання проекту'), ('klin', 'Клієнти'), ('life', 'Життєвий цикл'), ('free', 'Довільна Інформація')], default='free', max_length=4, verbose_name='Тема абзацу')),
                ('have_an_image', models.BooleanField(default=False)),
                ('rel_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logic.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSectionImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.projectsectiontype')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(max_length=50, verbose_name='Зміст')),
                ('main', models.TextField(max_length=300, verbose_name='Головна частина')),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logic.projectsectiontype')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='projectTeams',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='logic.workersteam', verbose_name="Пов'язана проєктна команда"),
        ),
        migrations.AddField(
            model_name='project',
            name='rel_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name="Пов'язаний менеджер"),
        ),
        migrations.CreateModel(
            name='ExpertiseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('eco', 'Екологія'), ('bio', 'Біотехнології'), ('mat', 'Матеріалознавство'), ('enr', 'Енергія'), ('all', 'Усі')], default='all', max_length=3, verbose_name='Тематика')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('main', models.TextField(blank=True, max_length=250, verbose_name='Тема')),
                ('full', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('rel_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Пов'язаний менеджер")),
                ('rel_projects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='logic.project')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('main', models.TextField(blank=True, max_length=250, verbose_name='Тема')),
                ('full', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logic.partner', verbose_name="Пов'язаний Участник")),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logic.project', verbose_name="Пов'язаний Проєкт")),
                ('rel_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Пов'язаний менеджер")),
            ],
        ),
    ]
