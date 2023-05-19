# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----External Imports-----
from .. import models as local_models
from ... import mixins as development_mixins
# endregion


@django.contrib.admin.register(local_models.Project)
class ProjectAdmin(
        development_mixins.admin.completion.Completion,
        utils.admin.admin.ReadonlyFieldsOnCRUD
    ):
    # region			   -----Table View-----
    list_display = [
        "title", "jira_code", "current_status", "sale_status", "development_progress_bar", 
        "delivery_progress_bar", "stages_link", "features_link", 
        "tasks_link"
    ]

    read_only_fields_on_update = ["jira_code"]

    readonly_fields = [
        "development_progress_bar", 
        "delivery_progress_bar"
    ]

    list_filter = [
        "current_status", 
        "sale_status"
    ]

    list_editable = [
        "current_status",
        "sale_status"
    ]

    search_fields = ["title"]

    ordering = ["title"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": [
                "jira_code",
                "title"
            ]
        }],
        ["Statuses", {
            "fields": [
                "current_status",
                "sale_status"
            ]
        }]
    ]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_related_objects(
        short_description=_("Features"),
        attribute="features"
    )
    def features_link(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return _("Features")
    

    @utils.admin.decorators.to_related_objects(
        short_description=_("Stages"),
        attribute="stages"
    )
    def stages_link(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return _("Stages")
    

    @utils.admin.decorators.to_related_objects(
        short_description=_("Tasks"),
        attribute="tasks"
    )
    def tasks_link(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return _("Tasks")
    # endregion