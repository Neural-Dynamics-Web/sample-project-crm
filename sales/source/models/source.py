# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import utils
# endregion


class Source(
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
        verbose_name_plural = _("Sources")
        verbose_name = _("Source")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return f"{self.title}"
    # endregion