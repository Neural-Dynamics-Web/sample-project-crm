# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
# endregion


class StartDate(django.db.models.Model):
    # region		    -----Date Calculation-----
    start_date = django.db.models.DateTimeField(
        verbose_name=_("Start Date"),
        blank=False,
        null=True
    )
    # endregion

    # region		  -----Similar Calculations-----
    def calculate_start_date_field(self,
            relation: typing.AnyStr
        ) -> typing.Dict:
        if self.id and relation:
            aggregation = {
                "start_date": django.db.models.Min(
                    f"{relation}__start_date"
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