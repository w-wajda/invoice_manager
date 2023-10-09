from django.db import models
from django.utils.translation import gettext as _

from users.models import User


class Accountant(models.Model):
    name = models.CharField(_("Name"), max_length=100, null=True)
    email = models.EmailField(_("Email"))
    user = models.ForeignKey(
        User, verbose_name=_("User"), on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("accountants")