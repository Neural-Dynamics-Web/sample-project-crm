# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
# endregion


class Code(django.db.models.Model):
    # region			  -----Informations-----
    code = django.db.models.CharField(
        verbose_name=_("Code"),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    # endregion