# region				-----External Imports-----
import django
# endregion

# region				-----External Imports-----
from ... import mixins as development_mixins
from .. import models as local_models
# endregion


@django.contrib.admin.register(local_models.Bug)
class BugAdmin(django.contrib.admin.ModelAdmin):
    # region			   -----Table View-----
    list_filter = [
        development_mixins.admin.filters.ProjectFilter,
        development_mixins.admin.filters.TaskFilter,
    ]
    
    list_display = ["title", "project", "task"]

    autocomplete_fields = ["task"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title", "description"]
        }],
        ["Relations", {
            "fields": ["task"]
        }]
    ]
    # endregion