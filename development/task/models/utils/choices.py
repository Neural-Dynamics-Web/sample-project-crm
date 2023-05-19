# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
# endregion


qa_status_list = [
    ("waiting", _("Waiting")),
    ("ready_to_test", _("Ready To Test")),
    ("passed", _("Passed")),
    ("reverted", _("Reverted"))
]

status_list = [
    ("created", _("Created")),
    ("in_progress", _("In Progress")),
    ("on_validation", _("On Validation")),
    ("completed", _("Completed"))
]

complexity_list = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
]