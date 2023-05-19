# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
# endregion


class Dates(django.db.models.Model):
    # region			      -----Dates----
    created_at = django.db.models.DateTimeField(
        default=django.utils.timezone.now,
        verbose_name=_("Created At"),
        blank=True,
        null=True
    )

    payment_date = django.db.models.DateField(
        verbose_name=_("Payment Date"),
        blank=False,
        null=True
    )

    actual_date = django.db.models.DateField(
        verbose_name=_("Actual Date"),
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion