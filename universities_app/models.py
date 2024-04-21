# from django.db import models
# from django.utils.translation import gettext_lazy as _

# # Create your models here.
# class Faculty(models.Model):
#     name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Faculty Name'))
#     description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
#     dean = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Dean Name'))

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = _('Faculty')
#         verbose_name_plural = _('Faculties')
#         ordering = ['name']

# class Subject(models.Model):
#     name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Subject Name'))
#     description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
#     syllabus = models.FileField(upload_to='syllabus/', null=True, blank=True, verbose_name=_('Syllabus'))
#     faculties = models.ManyToManyField(Faculty, related_name='subjects', verbose_name=_('Faculties'))
#     max_students = models.PositiveIntegerField(default=30, verbose_name=_('Max Students'))

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = _('Subject')
#         verbose_name_plural = _('Subjects')
#         ordering = ['faculties', 'name']