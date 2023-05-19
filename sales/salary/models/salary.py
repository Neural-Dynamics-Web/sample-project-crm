# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import utils
# endregion


class Salary(
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    amount = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Amount ($)"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=True
    )

    premium = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Premium ($)"),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=True
    )
    # endregion

    # region			    -----Relation-----
    staff = django.db.models.OneToOneField(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Staff"),
        related_name="salary",
        to="staff.Staff",
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        verbose_name_plural = _("Salaries")
        verbose_name = _("Salary")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.id)
    # endregion