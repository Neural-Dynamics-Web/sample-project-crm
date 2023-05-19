# region				-----External Imports-----
import django_lifecycle
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
        when_any=[
            "actual_date",
            "status", 
            "amount"
        ],
        has_changed=True,
        priority=0.000
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_DELETE,
        priority=0.000
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_CREATE,
        priority=0.000
    )
    def update_invoice_current_amount(self) -> None:
        output_field = django.db.models.DecimalField()
        invoice = self.invoice
        fields = [
            "current_amount"
        ]
        aggregations = {}

        for field in fields:
            aggregations[field] =\
                django.db.models.functions.Coalesce(
                    django.db.models.Sum(
                        "payments__amount",
                        filter=django.db.models.Q(
                            payments__status="completed"
                        ),
                        output_field=output_field
                    ),
                    decimal.Decimal(0.00)
                )
        
        result = invoice.__class__\
            .objects.filter(id=invoice.id)\
            .prefetch_related("payments")\
            .aggregate(**aggregations)
        
        for key, value in result.items():
            setattr(invoice, key, value)
        
        invoice.save()
    # endregion