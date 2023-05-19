# region				-----External Imports-----
import django
# endregion

# region				-----External Imports-----
from .. import models as local_models
# endregion


@django.contrib.admin.register(local_models.Department)
class DepartmentAdmin(django.contrib.admin.ModelAdmin):
    # region			   -----Table View-----
    list_display = ["title"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["title"]
        }]
    ]
    # endregion