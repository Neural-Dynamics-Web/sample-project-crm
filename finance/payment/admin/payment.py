# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----External Imports-----
from .. import models as local_models
# endregion


@django.contrib.admin.register(local_models.Payment)
class PaymentAdmin(
        utils.admin.admin.ReadonlyFieldsOnCRUD
    ):
    # region			   -----Table View-----
    list_display = [
        "id", "status", "invoice_link", "payment_date", "amount"
    ]

    read_only_fields_on_update = ["invoice"]

    list_filter = ["status", "invoice"]

    list_select_related = ["invoice"]

    autocomplete_fields = ["invoice"]

    readonly_fields = ["created_at"]

    list_editable = ["status"]

    search_fields = ["id"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["status", "amount"]
        }],
        ["Dates", {
            "fields": ["payment_date", "created_at"]
        }],
        ["Relations", {
            "fields": ["invoice"]
        }]
    ]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_change_link(
        short_description=_("Invoice"),
        ordering="invoice__id",
        attribute="invoice"
    )
    def invoice_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion