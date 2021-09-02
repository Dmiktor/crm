from venv import logger
from django import forms
from django.core.exceptions import ValidationError
from django.forms import EmailInput, URLInput, CheckboxInput, TextInput, Textarea, Select
from django.shortcuts import get_object_or_404
from image_cropping import ImageCropWidget

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('main', 'full', 'date')
        widgets = {
            'main': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть тему  вчиненої дії'
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть короткий опис вчиненої дії',
            }),

            'date': DateInput()
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('name',
                  'surname',
                  'nameEn',
                  'surnameEn',
                  'email',
                  'phone',
                  'phone2',
                  'Telegram',
                  'info',
                  'adress',
                  'notion',
                  'linkedIn',
                  'personal_page',
                  'skype',
                  'fb',
                  'valid',
                  )
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше ім`я Українською'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше прізвище Українською'
            }),
            'nameEn': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше ім`я Англійською'
            }),
            'surnameEn': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше прізвище Англійською'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш Email'
            }),
            'info': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Доп. інформація',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер вашого телефону',
            }),
            'phone2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Додатковий номер вашого телефону',
            }),
            'adress': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша адресса',
            }),
            'Telegram': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш Telegram'
            }),
            'skype': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш Skype'
            }),
            'notion': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Посилання на ваш Notion',
            }),
            'linkedIn': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Посилання на ваш linkedIn',
            }),
            'personal_page': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Посилання на вашу персональну сторінку',
            }),
            'fb': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Посилання на ваш Facebook',
            }),
            'valid': CheckboxInput(attrs={
                'label': 'Ви даєте право на обробку ваших персональних даних?',
                'class': 'form-check-input'
            }),
        }

    def clean_valid(self):
        valid = self.cleaned_data['valid']
        if not valid:
            raise ValidationError(
                "Ви не дали нам право на обробку ваших даних! Без цього ми не маємо право внести вас в систему.")
        return valid


class PartnerFormSecond(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('isWorker', 'isSeviceGiver', 'isInvestor', 'isStudent',)
        widgets = {
            'isWorker': CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Вы Розробник?',
            }),
            'isSeviceGiver': CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Сервіси?',
            }),
            'isInvestor': CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Інвестор?',
            }),
            'isStudent': CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Студент?',
            }),
        }


class WorkerProfileReg(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = ('org', 'position')
        widgets = {
            'org': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Установа де ви працюєте'
            }),
            'position': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша посада'
            }),
        }


class WorkersTeamReg(forms.ModelForm):
    class Meta:
        model = WorkersTeam
        fields = ('titleW',)
        widgets = {
            'titleW': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва вашої проектної команди *не обов`язково',
            }),
        }


class ProjectReg(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'main', 'category', 'projectStage',)
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коротка назва розробки'
            }),
            'main': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сутність та стислий опис',
            }),
            'category': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Галузь',
            }),
            'projectStage': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Ступінь готовності розробки',
            }),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = ProjectSectionType
        fields = ('type', 'have_an_image')
        widgets = {
            'type': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Тип',
            }),
            'valid': CheckboxInput(attrs={
                'label': 'Додати зображення до Секціі?',
                'class': 'form-check-input'
            }),
        }


class SectionMainForm(forms.ModelForm):
    class Meta:
        model = ProjectSection
        fields = ('header', 'main')
        widgets = {
            'header': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'main': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Головна частина',
            }),
        }


class SectionImgForm(forms.ModelForm):
    class Meta:
        model = ProjectSectionImg
        fields = ('img',)


class ExpertiseRequestForm(forms.ModelForm):
    class Meta:
        model = ExpertiseRequest
        fields = ('main', 'full', 'date', 'category', 'rel_Section')
        widgets = {
            'rel_Section': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Повьязана секція',
            }),
            'category': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Галузь',
            }),
            'main': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть тему  вчиненої дії'
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть короткий опис вчиненої дії',
            }),

            'date': DateInput()
        }

class ExpertiseAnswerForm(forms.ModelForm):
    class Meta:
        model = ExpertiseAnswer
        fields = ('main', 'full', 'date', )
        widgets = {
            'main': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть тему  вчиненої дії'
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть короткий опис вчиненої дії',
            }),
            'date': DateInput()
        }
