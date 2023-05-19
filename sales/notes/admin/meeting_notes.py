# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----External Imports-----
from .. import models as local_models
# endregion


@django.contrib.admin.register(local_models.MeetingNote)
class MeetingNoteAdmin(
        utils.admin.admin.ReadonlyFieldsOnCRUD
    ):
    # region			   -----Table View-----
    read_only_fields_on_update = ["meeting_date", "audio", "deal"]

    readonly_fields = ["title", "project", "transcript"]

    list_filter = ["deal", "project", "status"]

    list_select_related = ["deal", "project"]

    list_display = [
        "title", "meeting_date", "status",
        "project_link", "deal_link"
    ]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title", "audio", "meeting_date"]
        }],
        ["Transcript", {
            "fields": ["prompt", "text", "transcript"]
        }],
        ["Relations", {
            "fields": [
                "project",
                "deal"
            ]
        }]
    ]
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
        short_description=_("Deal"),
        ordering="deal__title",
        attribute="deal"
    )
    def deal_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion