# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----External Imports-----
from .. import models as local_models
# endregion


@django.contrib.admin.register(local_models.Contact)
class ContactAdmin(django.contrib.admin.ModelAdmin):
    # region			   -----Table View-----
    list_display = [
        "company", "name", "email", "position", "telegram", "phone",
        "lead_status", "last_call", "source_link", "deals_link"
    ]

    list_editable = ["lead_status", "last_call"]

    select_related_list = ["source"]

    list_filter = ["country"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["name", "company", "position", "lead_status"]
        }],
        ["Contacts", {
            "fields": ["email", "telegram", "phone", "last_call"]
        }],
        ["Relation", {
            "fields": ["country", "source"]
        }]
    ]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_related_objects(
        short_description=_("Deals"),
        attribute="deals"
    )
    def deals_link(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return _("Deals")
    
    
    @utils.admin.decorators.to_change_link(
        short_description=_("Source"),
        ordering="source__title",
        attribute="source"
    )
    def source_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion