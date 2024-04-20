from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts_app.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Last Name'))
    personal_number = models.CharField(max_length=11, null=False, blank=False, verbose_name=_('Personal Number'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'personal_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
