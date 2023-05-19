# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
# endregion


status_list = [
    ("awaiting", _("Awaiting")),
    ("completed", _("Completed")),
    ("outdated", _("Outdated"))
]