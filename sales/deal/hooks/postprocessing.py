# region				-----External Imports-----
import django_lifecycle
import datetime
import development
import finance
import decimal
import django
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PostprocessingHandlers(object):
    # region			  -----Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        has_changed=True,
        priority=0.000,
        when="status",
        is_now="win"
    )
    def generate_invoice_and_stage(self) -> None:
        next_week = django.utils.timezone.now().today()\
                  + datetime.timedelta(weeks=1)

        invoice = finance.models.Invoice\
            .objects.create(
                expected_amount=self.amount,
                payment_date=next_week,
                project=self.project,
                status="awaiting",
                stage=self.stage,
                title=self.title,
                deal=self
            )
    # endregion