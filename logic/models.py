from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from taggit.managers import TaggableManager

ALL = 'all'
ECOLOGY = 'eco'
BIOTECH = 'bio'
MATERIAL_SCIENCES = 'mat'
ENERGY = 'enr'

Category = [
    (ECOLOGY, 'Екологія'),
    (BIOTECH, 'Біотехнології'),
    (MATERIAL_SCIENCES, 'Матеріалознавство'),
    (ENERGY, 'Енергія'),
    (ALL, 'Усі'),
]


class Event(models.Model):
    INTERNAL = 'int'
    EXTERNAL = 'ext'
    PUB = [
        (INTERNAL, 'Внутрішній'),
        (EXTERNAL, 'Зовнішній'),
    ]
    title = models.CharField("Назва", max_length=200)
    slug = models.SlugField("Унікальна Адресса", max_length=255, blank=True, unique=True)
    date = models.DateField("Дата", blank=True, null=True)
    main = models.TextField("Короткий текст", blank=True, max_length=600)
    full = RichTextField("Повний текст", blank=True, null=True)
    category = models.CharField("Тематика",
                                max_length=3,
                                choices=Category,
                                default=ALL,
                                )
    pub = models.CharField("Публічність",
                           max_length=3,
                           choices=PUB,
                           default=INTERNAL,
                           )

    def __str__(self):
        return self.slug


class Partner(models.Model):
    name = models.CharField("Ім'я", max_length=30)
    surname = models.CharField("Прізвище", max_length=30)
    nameEn = models.CharField("Ім'я Англійською", max_length=30, blank=True)
    surnameEn = models.CharField("Прізвище Англійською", max_length=30, blank=True)
    email = models.EmailField("Електронна пошта ", unique=True)
    phone = PhoneNumberField("Телефон", blank=False, unique=True)
    phone2 = PhoneNumberField("Телефон доп.", null=True, blank=True, unique=True)
    GoogleDisk = models.URLField("Посилання на гугл диск", blank=False, default="#")
    Telegram = models.CharField("Telegram", max_length=30, blank=True, )
    info = RichTextField("Інф.", blank=True, max_length=600)
    adress = models.CharField("Адреса", max_length=70, blank=True)
    notion = models.CharField("Notion", blank=True, max_length=30)
    linkedIn = models.URLField("Посилання на linkedIn", blank=True, default="#")
    personal_page = models.URLField("Посилання на персональну сторінку", blank=True, default="#")
    skype = models.CharField("Skype", blank=True, max_length=30)
    fb = models.URLField("Посилання на Facebook", blank=True, default="#")
    isWorker = models.BooleanField("Розробник?", default=False)
    isPartner = models.BooleanField("Партнер?", default=False)
    isSeviceGiver = models.BooleanField("Надавач сервісів?", default=False)
    isSeviceTaker = models.BooleanField("Користувач сервісів?", default=False)
    isInvestor = models.BooleanField("Інвестор?", default=False)
    isStudent = models.BooleanField("Студент?", default=False)

    def __str__(self):
        return self.name


class WorkerProfile(models.Model):
    partner = models.OneToOneField(Partner, on_delete=models.CASCADE, verbose_name="Пов'язаний Участник")
    org = models.CharField("Установа", max_length=40, blank=True)
    position = models.CharField("Посада", max_length=30, blank=True)

    def __str__(self):
        return self.partner.name


class WorkersTeam(models.Model):
    title = models.CharField("Назва команди", max_length=60)
    rel_partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=True, blank=True,
                                    verbose_name="Відповідальна за команду особа")
    workers = models.ManyToManyField(WorkerProfile, verbose_name="Пов'язані розробники")

    def __str__(self):
        return self.title


class Project(models.Model):
    TEH = 'teh'
    SER = 'ser'
    TYP = [
        (TEH, 'Технологічні'),
        (SER, 'Сервісні'),
    ]
    title = models.CharField("Назва проєкту", max_length=60)
    main = RichTextField("Короткий опис проєкту", blank=True, max_length=600)
    category = models.CharField("Тематика",
                                max_length=3,
                                choices=Category,
                                default=ALL,
                                )
    projectType = models.CharField("Тип проєкту",
                                   max_length=3,
                                   choices=TYP,
                                   default=TEH,
                                   )
    projectTeams = models.OneToOneField(WorkersTeam, on_delete=models.PROTECT, null=True, blank=True,
                                        verbose_name="Пов'язана проєктна команда")


def __str__(self):
    return self.title


class Action(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пов'язаний "
                                                                                                       "Участник")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пов'язаний "
                                                                                                       "Проєкт")
    rel_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                    verbose_name="Пов'язаний менеджер")
    date = models.DateField("Дата", blank=True, null=True)
    main = models.TextField("Тема", blank=True, max_length=250)
    full = models.TextField("Опис", blank=True, null=True)

    def __str__(self):
        return self.main


class ServiceProvider(models.Model):
    partner = models.OneToOneField(Partner, on_delete=models.CASCADE, verbose_name="Пов'язаний Участник")

    def __str__(self):
        return self.partner.name


class RecipientServices(models.Model):
    partner = models.OneToOneField(Partner, on_delete=models.CASCADE, verbose_name="Пов'язаний Участник")
    partnerTags = TaggableManager("Список зацікавивших тегів")

    def __str__(self):
        return self.partner.name


class Service(models.Model):
    title = models.CharField("Назва сервісу", max_length=60)
    recipient_of_services = models.ManyToManyField(RecipientServices, blank=True, verbose_name="Ожержувачі "
                                                                                               "сервісів")
    service_providers = models.ManyToManyField(ServiceProvider, verbose_name="Відровідальні надувачі сервісів")
    rel_projects = models.ManyToManyField(Project, blank=True, verbose_name="Пов'язані проєкти")
    partnerTags = TaggableManager("Список тегів сервісу")
    full = RichTextField("Опис", blank=True, null=True)
    price = models.DecimalField("Вартість у грн.", max_digits=10, decimal_places=2)
    terms = models.TextField("Умови надання", blank=True, max_length=250)
    target = models.TextField("Цільова аудиторія", blank=True, max_length=600)
    category = models.CharField("Цільова тематика",
                                max_length=3,
                                choices=Category,
                                default=ALL,
                                )

    def __str__(self):
        return self.title


@receiver(post_save, sender=Partner)
def create_partner_profile(sender, instance, created, **kwargs):
    if instance.isWorker:
        if created:
            WorkerProfile.objects.create(partner=instance)
    if instance.isSeviceGiver:
        if created:
            ServiceProvider.objects.create(partner=instance)
    if instance.isSeviceTaker:
        if created:
            RecipientServices.objects.create(partner=instance)


@receiver(post_save, sender=Partner)
def save_user_profile(sender, instance, **kwargs):
    if instance.isWorker:
        if hasattr(instance, 'workerprofile'):
            instance.workerprofile.save()
        else:
            WorkerProfile.objects.create(partner=instance)
    else:
        if hasattr(instance, 'workerprofile'):
            instance.workerprofile.delete()
    if instance.isSeviceGiver:
        if hasattr(instance, 'serviceprovider'):
            instance.serviceprovider.save()
        else:
            ServiceProvider.objects.create(partner=instance)
    else:
        if hasattr(instance, 'serviceprovider'):
            instance.serviceprovider.delete()
    if instance.isSeviceTaker:
        if hasattr(instance, 'recipientservices'):
            instance.recipientservices.save()
        else:
            RecipientServices.objects.create(partner=instance)
    else:
        if hasattr(instance, 'recipientservices'):
            instance.recipientservices.delete()
