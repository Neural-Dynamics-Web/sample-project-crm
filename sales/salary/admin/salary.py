# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion

# region				-----External Imports-----
from .. import models as local_models
# endregion


@django.contrib.admin.register(local_models.Salary)
class SalaryAdmin(
        utils.admin.admin.ReadonlyFieldsOnCRUD
    ):
    # region			   -----Table View-----
    list_display = [
        "id", "staff_link", "amount", "premium"
    ]
    
    read_only_fields_on_update = ["staff"]

    select_related_fields = ["staff"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["amount", "premium"]
        }],
        ["Relations", {
            "fields": ["staff"]
        }]
    ]
    # endregion

    # region			  -----Table Method-----
    @utils.admin.decorators.to_change_link(
        short_description=_("Staff"),
        ordering="staff__email",
        attribute="staff"
    )
    def staff_link(self, 
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return instance
    # endregion