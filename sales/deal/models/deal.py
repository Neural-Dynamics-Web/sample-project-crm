# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_lifecycle
import django_ckeditor_5
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import hooks as deal_hooks
from .utils import choices as local_choices
# endregion


class Deal(
        deal_hooks.postprocessing.PostprocessingHandlers,
        deal_hooks.preprocessing.PreprocessingHandlers,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    description = django_ckeditor_5.fields.CKEditor5Field(
        verbose_name=_("Description"),
        config_name='extends',
        blank=True,
        null=True
    )

    development_status = django.db.models.CharField(
        choices=local_choices.development_status_list,
        verbose_name=_("Development Status"),
        default="rated",
        max_length=255,
        blank=False
    )

    amount = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Amount ($)"),
        decimal_places=2,
        max_digits=10,
        blank=True,
        null=True
    )

    estimate = django.db.models.FileField(
        verbose_name=_("Estimate"),
        upload_to="estimates",
        blank=True,
        null=True
    )

    status = django.db.models.CharField(
        choices=local_choices.status_list,
        verbose_name=_("Sale Status"),
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

    # region		    -----Date Calculation-----
    actual_end_date = django.db.models.DateField(
        verbose_name=_("Actual End Date"),
        blank=True,
        null=True
    )
    
    start_date = django.db.models.DateField(
        verbose_name=_("Start Date"),
        blank=True,
        null=True
    )

    end_date = django.db.models.DateField(
        verbose_name=_("End Date"),
        blank=True,
        null=True
    )
    # endregion

    # region			    -----Relation-----
    assignee = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Sales Manager"),
        related_name="deals",
        to="staff.Staff",
        blank=False,
        null=True,
    )

    contact = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Contact"),
        related_name="deals",
        to="sales.Contact",
        blank=False,
        null=True,
    )

    project = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Project"),
        to="development.Project",
        related_name="deals",
        blank=True,
        null=True
    )

    stage = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Stage"),
        to="development.Stage",
        related_name="deals",
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        verbose_name_plural = _("Deals")
        verbose_name = _("Deals")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion