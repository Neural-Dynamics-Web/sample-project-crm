# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_lifecycle
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import hooks as feature_hooks
from ... import mixins as development_mixins
from .utils import choices as local_choices
# endregion


class Feature(
        development_mixins.models.delivery_end_dates.DeliveryEndDates,
        development_mixins.models.delivery_hour.DeliveryHour,
        feature_hooks.postprocessing.PostprocessingHandlers,
        feature_hooks.preprocessing.PreprocessingHandlers,
        development_mixins.models.completions.Completions,
        development_mixins.models.start_date.StartDate,
        development_mixins.models.jira.Jira,
        development_mixins.models.cost.Cost,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):

    # region			      -----Dates----
    created_at = django.db.models.DateTimeField(
        default=django.utils.timezone.now,
        verbose_name=_("Created At"),
        blank=True,
        null=True
    )
    # endregion

    # region			  -----Informations-----
    priority = django.db.models.CharField(
        choices=local_choices.priority_list,
        verbose_name=_("Priority"),
        max_length=255,
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

    # region			    -----Relation-----
    project = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Project"),
        to="development.Project",
        related_name="features",
        blank=True,
        null=True
    )

    stage = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        related_name="features",
        verbose_name=_("Stage"),
        to="development.Stage",
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Features")
        verbose_name = _("Feature")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion