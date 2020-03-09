import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created at"), blank=True, null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("updated at"), blank=True, null=True
    )

    class DoesNotExists(Exception):
        pass

    class Meta:
        abstract = True
