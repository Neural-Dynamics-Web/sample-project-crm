# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import decimal
import django
import typing
import utils
# endregion


class DeliveryHour(django.db.models.Model):
    # region		    -----Time Calculation-----
    delivery_hour = django.db.models.DecimalField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Delivery Hours"),
        default=decimal.Decimal(0.00),
        decimal_places=2,
        max_digits=10,
        blank=False
    )
    # endregion

    # region		  -----Similar Calculations-----
    def calculate_delivery_hour_field(self,
            relation: typing.AnyStr
        ) -> typing.Dict:
        if self.id and relation:
            aggregation = {
                "delivery_hour":\
                    django.db.models.functions.Coalesce(
                        django.db.models.Sum(
                            f"{relation}__delivery_hour"
                        ),
                        decimal.Decimal(0.00)
                    )
            }

            result = self.__class__\
                .objects.filter(id=self.id)\
                .prefetch_related(relation)\
                .aggregate(**aggregation)
        
        return result
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion