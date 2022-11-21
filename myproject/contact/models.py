import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    firstname = models.CharField(_('First Name'), max_length=100)
    lastname = models.CharField(_('Last Name'), max_length=100)
    phone = models.CharField(_('Phone'), max_length=20)
    def __str__(self):
        return str(self.firstname + self.lastname)