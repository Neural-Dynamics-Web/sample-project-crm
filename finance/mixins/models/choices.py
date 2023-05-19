# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
# endregion

# region				-----Internal Imports-----
from .utils import choices as local_choices
# endregion


class Choices(django.db.models.Model):
    # region			      -----Dates----
    status = django.db.models.CharField(
        choices=local_choices.status_list,
        verbose_name=_("Status"),
        default="waiting",
        max_length=255,
        blank=False
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion