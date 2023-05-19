# region				-----External Imports-----
import django
import celery
import logging
# endregion

# region				-----Internal Imports-----
from .. import models
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


@celery.shared_task(name="find_outdated_payments")
def find_outdated_payments():
    now = django.utils.timezone.now()

    outdated = models.payment.Payment.objects\
        .filter(payment_date__lt=now.today())\
        .exclude(status="completed")\
        .all()
    
    for payment in outdated:
        payment.status = "outdated"
        payment.save()