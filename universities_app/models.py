from django.db import models
from django.utils.translation import gettext_lazy as _


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
    faculties = models.ManyToManyField('Faculty', verbose_name=_('Faculties'), blank=True)
    students = models.ManyToManyField('Student', verbose_name=_('Student'), blank=True)
    lecturer = models.OneToOneField('Lecturer', on_delete=models.CASCADE, verbose_name=_('Lecturer'), blank=True)

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    # TODO implement custom user class to assign to user field in lecturer
    user = models.OneToOneField('PlainCustomUser', on_delete=models.CASCADE, primary_key=True, verbose_name=_('User'))
    name = models.CharField(max_length=200, verbose_name=_('Lecturer name'))
    surname = models.CharField(max_length=200, verbose_name=_('Lecturer surname'))

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Student(models.Model):
    # TODO implement custom user class to assign to user field in lecturer
    user = models.OneToOneField('PlainCustomUser', on_delete=models.CASCADE, primary_key=True, verbose_name=_('User'))
    name = models.CharField(max_length=200, verbose_name=_('Student name'))
    surname = models.CharField(max_length=200, verbose_name=_('Student surname'))
    subjects = models.ManyToManyField('Subject', verbose_name=_('Subject'), blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name=_('Faculty'), blank=True)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return f'{self.name} {self.surname}'


class PlainCustomUser(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')

    def __str__(self):
        return f'{self.username}'
