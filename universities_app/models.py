from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts_app.models import CustomUser

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Faculty name'), unique=True)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Subject name'), unique=True)
    description = models.TextField(verbose_name=_('Description'))
    syllabus = models.FileField(verbose_name=_('Syllabus'), upload_to='syllabus/')

    faculties = models.ManyToManyField('Faculty', verbose_name=_('Faculties'))
    lecturer = models.OneToOneField('Lecturer', on_delete=models.CASCADE, verbose_name=_('Lecturer'))
    student = models.ManyToManyField('Student', verbose_name=_('Student'), limit_choices_to={'id__lte': 7})

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.name
    

class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name=_('User'))
    first_name = models.CharField(max_length=200, verbose_name=_('Lecturer first name'), blank=True)
    last_name = models.CharField(max_length=200, verbose_name=_('Lecturer last name'), blank=True)

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name=_('User'))
    first_name = models.CharField(max_length=200, verbose_name=_('Student first name'), blank=True)
    last_name = models.CharField(max_length=200, verbose_name=_('Student last name'), blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name=_('Faculty'))

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'