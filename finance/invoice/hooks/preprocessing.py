# region				-----External Imports-----
import django_lifecycle
import django
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PreprocessingHandlers(object):
    # region			  -----Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        when_any=[
            "expected_amount",
            "current_amount",
            "actual_date"
        ],
        has_changed=True,
        priority=0.011
    )
    def calculate_actual_date(self) -> None:
        aggregations = {
            "actual_date": django.db.models.Max(
                "payments__actual_date"
            )
        }

        if self.completion >= 100:
            date = self.__class__\
                .objects.filter(id=self.id)\
                .prefetch_related("payments")\
                .aggregate(**aggregations)\
                ["actual_date"]

            self.actual_date = date
        else:
            self.actual_date = None
    

    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        when_any=[
            "expected_amount",
            "current_amount"
        ],
        has_changed=True,
        priority=0.000
    )
    def calculate_completion(self) -> None:
        try:
            completion = self.current_amount\
                       / self.expected_amount\
                       * 100
        except ZeroDivisionError:
            completion = 0

        self.completion = completion


    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        priority=0.010
    )
    def calculate_status(self) -> None:
        if self.completion >= 100:
            self.status = "completed"
        else:
            now = django.utils.timezone.now()
            outdated = self.payment_date\
                     < now.date()
            
            if outdated:
                self.status = "outdated"
            else:
                self.status = "awaiting"
    # endregion