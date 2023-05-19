# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
# endregion


class DeliveryEndDates(django.db.models.Model):
    # region		    -----Date Calculation-----
    actual_delivery_end_date = django.db.models.DateTimeField(
        verbose_name=_("Actual Delivery End Date"),
        blank=True,
        null=True
    )

    delivery_end_date = django.db.models.DateTimeField(
        verbose_name=_("Delivery End Date"),
        blank=True,
        null=True
    )
    # endregion

    # region		  -----Similar Calculations-----
    def calculate_delivery_date_fields(self,
            relation: typing.AnyStr
        ) -> typing.Dict:
        if self.id and relation:
            fields = [
                "actual_delivery_end_date",
                "delivery_end_date"
            ]
            aggregations = {}

            for field in fields:
                aggregations[field] =\
                    django.db.models.Max(
                       f"{relation}__{field}"
                    )
            
            result = self.__class__\
                .objects.filter(id=self.id)\
                .prefetch_related(relation)\
                .aggregate(**aggregations)
        
        return result
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion