# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import utils
# endregion


class Country(
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        unique=True,
        blank=False,
        null=True
    )
    # endregion
    
    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Countries")
        verbose_name = _("Country")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return f"{self.title}"
    # endregion