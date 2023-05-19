# region				-----External Imports-----
from django.contrib.auth.admin import UserAdmin
import django
# endregion

# region				-----External Imports-----
from .. import models as local_models
# endregion


class StaffAdmin(UserAdmin):
    # region			   -----Table View-----
    list_display = [
        "email", "first_name", "last_name", "department", "country", 
        "address", "phone", "linkedin", "job", "is_active",
        "type_of_payment"
    ]

    list_filter = ["department", "country", "type_of_payment"]

    readonly_fields = ["last_login"]

    list_editable = ["is_active"]
    # endregion

    # region			   -----Forms View-----
    fieldsets = [
        ["General", {
            "fields": ["username", "password"]
        }],
        ["Personal info", {
            "fields": ["first_name", "last_name"]
        }],
        ["Permissions", {
            "fields": [
                "is_active", "is_staff", "is_superuser", 
                "groups", "user_permissions"
            ],
        }],
        ["Important dates", {
            "fields": ["last_login", "joined_at"]
        }],
        ["Location", {
            "fields": ["country", "address"]
        }],
        ["Contacts", {
            "fields": ["phone", "linkedin", "email"]
        }],
        ["Additional Information", {
            "fields": ["department", "job", "type_of_payment"]
        }]
    ]
    # endregion

    # region			  -----Forms Method-----
    def has_delete_permission(self, 
            request: django.http.HttpRequest = None,
            obj: django.db.models.Model = None
        ) -> bool:
        return False
    # endregion


django.contrib.admin.site.register(
    local_models.Staff,
    StaffAdmin
)