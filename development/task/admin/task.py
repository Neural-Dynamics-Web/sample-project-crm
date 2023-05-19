# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----Internal Imports-----
from ... import mixins as development_mixins
from .. import services as local_services
from .. import models as local_models
from . import form as local_form
# endregion


@django.contrib.admin.register(local_models.Task)
class TaskAdmin(
        utils.admin.admin.ReadonlyFieldsOnCRUD
    ):
    # region			   -----Table View-----
    list_display = [
        "title", "jira_code", "project_link", "stage_link", "feature_link", 
        "rate", "status", "qa_status", "cost", "development_hour", "qa_hour", 
        "delivery_hour", "staff_link", "start_date", "development_end_date", 
        "delivery_end_date", "actual_delivery_end_date"
    ]
    
    list_select_related = ["project", "stage", "feature", "staff"]

    list_filter = [
        development_mixins.admin.filters.ProjectFilter,
        development_mixins.admin.filters.StageFilter,
        development_mixins.admin.filters.FeatureFilter,
        "status", "staff", "qa_status"
    ]

    autocomplete_fields = ["feature", "staff"]

    read_only_fields_on_update = ["feature"]

    list_editable = ["status", "qa_status"]

    search_fields = ["title"]

    ordering = ["title"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title", "description"]
        }],
        ["Statuses", {
            "fields": ["status", "qa_status"]
        }],
        ["Estimates ($)", {
            "fields": ["rate"]
        }],
        ["Estimates Time", {
            "fields": [
                "development_hour",
                "start_date",
                "actual_delivery_end_date"
            ]
        }],
        ["Relations", {
            "fields": [
                "feature",
                "staff"
            ]
        }]
    ]

    form = local_form.TaskForm
    # endregion

    # region			  -----Table Method-----
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
        short_description=_("Feature"),
        ordering="feature__title",
        attribute="feature"
    )
    def feature_link(self, 
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
        short_description=_("Staff"),
        ordering="staff__username",
        attribute="staff"
    )
    def staff_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion

    #! REMOVE LATER, AFTER TESTING
    def save_model(self, 
            request: django.http.HttpRequest, 
            obj: django.db.models.Model, 
            form: django.forms.Form, 
            change: typing.Dict
        ) -> None:
        try:
            was = self.model.objects.get(pk=obj.pk)\
                .actual_delivery_end_date
            now = obj.actual_delivery_end_date
        except self.model.DoesNotExist:
            was = obj.actual_delivery_end_date
            now = obj.actual_delivery_end_date

        super().save_model(
            request=request, 
            change=change, 
            form=form, 
            obj=obj
        )

        local_services.time_shift\
            .time_shift(
                task=obj,
                was=was,
                now=now
            )