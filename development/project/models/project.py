# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_lifecycle
import django
import utils
import uuid
# endregion

# region				-----Internal Imports-----
from .. import hooks as project_hooks
from ... import mixins as development_mixins
from .utils import choices as local_choices
# endregion


class Project(
        project_hooks.preprocessing.PreprocessingHandlers,
        development_mixins.models.completions.Completions,
        development_mixins.models.jira.Jira,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    current_status = django.db.models.CharField(
        choices=local_choices.current_status_list,
        verbose_name=_("Current Status"),
        max_length=255,
        blank=False,
        null=True
    )

    sale_status = django.db.models.CharField(
        choices=local_choices.sale_status_list,
        verbose_name=_("Sale Status"),
        max_length=255,
        blank=False,
        null=True
    )

    jira_code = django.db.models.CharField(
        verbose_name=_("Jira Code"),
        max_length=255,
        unique=True,
        blank=False,
        null=True
    )

    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Dates----
    created_at = django.db.models.DateTimeField(
        default=django.utils.timezone.now,
        verbose_name=_("Created At"),
        blank=False
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Projects")
        verbose_name = _("Project")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion