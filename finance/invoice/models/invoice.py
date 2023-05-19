# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_lifecycle
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import hooks as invoice_hooks
from ... import mixins as finance_mixins
# endregion


class Invoice(
        invoice_hooks.preprocessing.PreprocessingHandlers,
        finance_mixins.models.choices.Choices,
        finance_mixins.models.dates.Dates,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    completion = django.db.models.PositiveIntegerField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Completion (%)"),
        blank=True,
        default=0
    )

    expected_amount = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Expected Amount ($)"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=True
    )

    current_amount = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Current Amount ($)"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        default=0
    )

    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion
    
    # region			    -----Relation-----
    deal = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        related_name="invoices",
        verbose_name=_("Deal"),
        to="sales.Deal",
        blank=True,
        null=True
    )

    project = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Project"),
        to="development.Project",
        related_name="invoices",
        blank=True,
        null=True
    )

    stage = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        related_name="invoices",
        verbose_name=_("Stage"),
        to="development.Stage",
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Invoices")
        verbose_name = _("Invoice")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion