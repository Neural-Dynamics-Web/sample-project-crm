# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
# endregion


class Jira(django.db.models.Model):
    # region			  -----Informations-----
    jira_code = django.db.models.CharField(
        verbose_name=_("Jira Code"),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    jira_id = django.db.models.CharField(
        verbose_name=_("Jira ID"),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion