# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion


class Completions(django.db.models.Model):
    # region		 -----Completion Calculation-----
    development_completion = django.db.models.PositiveIntegerField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Development Completion (%)"),
        blank=True,
        default=0
    )

    delivery_completion = django.db.models.PositiveIntegerField(
        validators=[
            utils.models.validators.positive_validator
        ],
        verbose_name=_("Delivery Completion (%)"),
        blank=True,
        default=0
    )
    # endregion

    # region		  -----Similar Calculations-----
    def calculate_completion_fields(self,
            relation: typing.AnyStr
        ) -> typing.Dict:
        if self.id and relation:
            fields = [
                "development_completion",
                "delivery_completion"
            ]
            aggregations = {}

            for field in fields:
                aggregations[field] =\
                    django.db.models.Avg(
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