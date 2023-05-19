# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextField
import django_lifecycle
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import hooks as task_hooks
from ... import mixins as development_mixins
from .utils import choices as local_choices
from .utils import defaults as local_defaults
# endregion


class Task(
        development_mixins.models.delivery_end_dates.DeliveryEndDates,
        development_mixins.models.delivery_hour.DeliveryHour,
        task_hooks.postprocessing.PostprocessingHandlers,
        task_hooks.preprocessing.PreprocessingHandlers,
        development_mixins.models.start_date.StartDate,
        development_mixins.models.jira.Jira,
        development_mixins.models.cost.Cost,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region		    -----Date Calculation-----
    development_end_date = django.db.models.DateTimeField(
        verbose_name=_("Development End Date"),
        blank=True,
        null=True
    )

    start_date = django.db.models.DateTimeField(
        verbose_name=_("Start Date"),
        blank=False,
        null=True
    )
    # endregion

    # region			  -----Informations-----
    development_hour = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Development Hours"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=True
    )

    qa_hour = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("QA Hours"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=True
    )

    rate = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Rate ($)"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=True
    )

    qa_status = django.db.models.CharField(
        choices=local_choices.qa_status_list,
        verbose_name=_("QA Status"),
        default="waiting",
        max_length=255,
        blank=False
    )

    description = MDTextField(
        default=local_defaults.description,
        verbose_name=_("Description"),
        blank=False
    )

    status = django.db.models.CharField(
        choices=local_choices.status_list,
        verbose_name=_("Status"),
        default="created",
        max_length=255,
        blank=False
    )

    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion

    # region			    -----Relation-----
    staff = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Staff"),
        related_name="tasks",
        to="staff.Staff",
        blank=False,
        null=True,
    )

    feature = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Feature"),
        to="development.Feature",
        related_name="tasks",
        blank=False,
        null=True
    )

    project = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Project"),
        to="development.Project",
        related_name="tasks",
        blank=True,
        null=True
    )

    stage = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Stage"),
        to="development.Stage",
        related_name="tasks",
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        verbose_name_plural = _("Tasks")
        verbose_name = _("Task")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion