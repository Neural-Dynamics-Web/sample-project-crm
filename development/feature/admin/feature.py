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


@django.contrib.admin.register(local_models.Feature)
class FeatureAdmin(
        development_mixins.admin.completion.Completion,
        utils.admin.admin.ReadonlyFieldsOnCRUD
    ):
    # region			   -----Table View-----
    list_display = [
        "title", "jira_code", "project_link", "stage_link", "priority", 
        "cost", "delivery_hour", "start_date", "delivery_end_date", 
        "actual_delivery_end_date", "development_progress_bar", 
        "delivery_progress_bar", "tasks_link"
    ]

    list_filter = [
        development_mixins.admin.filters.ProjectFilter,
        development_mixins.admin.filters.StageFilter,
        "priority"
    ]

    list_select_related = ["project", "stage"]

    read_only_fields_on_update = ["stage"]

    autocomplete_fields = ["stage"]

    readonly_fields = [
        "development_progress_bar", 
        "delivery_progress_bar",
        "created_at",
        "project"
    ]

    list_editable = ["priority"]

    search_fields = ["title"]

    ordering = ["title"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title", "priority"]
        }],
        ["Relations", {
            "fields": ["stage"]
        }]
    ]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_related_objects(
        short_description=_("Tasks"),
        attribute="tasks"
    )
    def tasks_link(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return _("Tasks")
    

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
    # endregion