# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----External Imports-----
from .. import models as local_models
from ... import mixins as finance_mixins
# endregion


@django.contrib.admin.register(local_models.Invoice)
class InvoiceAdmin(
        finance_mixins.admin.completion.Completion
    ):
    # region			   -----Table View-----
    list_display = [
        "title", "status", "project_link", "stage_link", "deal_link", 
        "payment_date", "actual_date", "expected_amount", "current_amount", 
        "progress_bar", "payments_link"
    ]

    list_filter = ["project", "stage", "deal", "status"]

    list_select_related = ["project", "stage", "deal"]

    readonly_fields = [
        "created_at", "project", "current_amount", 
        "deal", "status", "actual_date"
    ]

    search_fields = ["title"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title", "status"]
        }],
        ["Dates", {
            "fields": ["payment_date", "actual_date", "created_at"]
        }],
        ["Relations", {
            "fields": ["project", "stage", "deal"]
        }],
        ["Finance", {
            "fields": ["expected_amount", "current_amount"]
        }]
    ]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_related_objects(
        short_description=_("Payments"),
        attribute="payments"
    )
    def payments_link(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return _("Payments")
    
    
    @utils.admin.decorators.to_change_link(
        short_description=_("Project"),
        ordering="project__title",
        attribute="project"
    )
    def project_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    
    
    @utils.admin.decorators.to_change_link(
        short_description=_("Stage"),
        ordering="stage__title",
        attribute="stage"
    )
    def stage_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    

    @utils.admin.decorators.to_change_link(
        short_description=_("Deal"),
        ordering="deal__id",
        attribute="deal"
    )
    def deal_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion

    # region			  -----Forms Method-----
    def has_add_permission(self, 
            request: django.http.HttpRequest
        ) -> bool:
        return False
    # endregion