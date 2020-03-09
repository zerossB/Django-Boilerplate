import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


# Create your models here.
class User(AbstractUser, BaseModel):

    uuid = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)
    jwt = models.CharField(
        _("JWT Field"),
        max_length=255,
        unique=True,
        editable=False,
        blank=True,
        null=True,
    )

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"uuid": self.uuid})
