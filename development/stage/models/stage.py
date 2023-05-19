# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_lifecycle
import django
import utils
import uuid
# endregion

# region				-----Internal Imports-----
from .. import hooks as stage_hooks
from ... import mixins as development_mixins
# endregion


class Stage(
        development_mixins.models.delivery_end_dates.DeliveryEndDates,
        development_mixins.models.delivery_hour.DeliveryHour,
        stage_hooks.postprocessing.PostprocessingHandlers,
        development_mixins.models.completions.Completions,
        stage_hooks.preprocessing.PreprocessingHandlers,
        development_mixins.models.start_date.StartDate,
        development_mixins.models.jira.Jira,
        development_mixins.models.cost.Cost,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region			    -----Relation-----
    project = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Project"),
        to="development.Project",
        related_name="stages",
        blank=False,
        null=True
    )
    # endregion

    # region			  -----Informations-----
    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Stages")
        verbose_name = _("Stage")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion