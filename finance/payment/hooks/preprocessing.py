# region				-----External Imports-----
import django_lifecycle
import decimal
import django
import logging
import utils
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PreprocessingHandlers(object):
    # region		  -----Similar Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        is_now="completed",
        priority=0.000,
        when="status"
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        is_now="completed",
        priority=0.000,
        when="status"
    )
    def calculate_actual_date(self) -> None:
        self.actual_date = django.utils.timezone.now().date()
        pass
    # endregion