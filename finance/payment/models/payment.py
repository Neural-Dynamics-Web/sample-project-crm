# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_lifecycle
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import hooks as payment_hooks
from ... import mixins as finance_mixins
# endregion


class Payment(
        payment_hooks.postprocessing.PostprocessingHandlers,
        payment_hooks.preprocessing.PreprocessingHandlers,
        finance_mixins.models.choices.Choices,
        finance_mixins.models.amount.Amount,
        finance_mixins.models.dates.Dates,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region			    -----Relation-----
    invoice = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Invoice"),
        related_name="payments",
        to="finance.Invoice",
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Payments")
        verbose_name = _("Payment")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.id)
    # endregion