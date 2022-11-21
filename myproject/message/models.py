import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class Message(models.Model):
    contact = models.ForeignKey("contact.Contact", verbose_name=_(""), on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    otp = models.TextField(max_length=6)
    def __str__(self):
        return str(self.otp)