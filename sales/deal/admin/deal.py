# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----Internal Imports-----
from .. import models as local_models
from . import form as local_form
# endregion


@django.contrib.admin.register(local_models.Deal)
class DealAdmin(
        django.contrib.admin.ModelAdmin
    ):
    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title", "status", "development_status", "description"]
        }],
        ["Dates", {
            "fields": ["start_date", "end_date", "actual_end_date"]
        }],
        ["Relations", {
            "fields": ["project", "stage", "contact", "assignee"]
        }],
        ["Finance", {
            "fields": ["amount"]
        }],
        ["Files", {
            "fields": ["estimate"]
        }]
    ]

    form = local_form.DealForm
    # endregion
    
    # region			   -----Table View-----
    list_display = [
        "title", "status", "development_status", "project_link", 
        "estimate", "amount", "assignee_link",
        "start_date", "end_date", 
        "actual_end_date"
    ]

    list_filter = ["status", "development_status", "assignee"]
    
    list_editable = [
        "estimate", "development_status", "start_date", 
        "end_date", "actual_end_date"
    ]

    readonly_fields = ["stage"]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_change_link(
        short_description=_("Sales Manager"),
        ordering="assignee__email",
        attribute="assignee"
    )
    def assignee_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    
    @utils.admin.decorators.to_change_link(
        short_description=_("Project"),
        ordering="project__title",
        attribute="project"
    )
    def project_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion

    # region			  -----Form Methods-----
    def get_readonly_fields(self,
            request: django.http.HttpRequest = None,
            obj: django.db.models.Model = None
        ) -> typing.List[str]:
        if obj and obj.project:
            result_fields = tuple(self.readonly_fields)\
                          + ("project", )
            return result_fields
        return self.readonly_fields
    # endregion