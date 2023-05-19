# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import utils
# endregion


class Department(
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    title = django.db.models.CharField(
        verbose_name=_("Tilte"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Departments")
        verbose_name = _("Department")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion