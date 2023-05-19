# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import utils
# endregion


class Amount(django.db.models.Model):
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
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion