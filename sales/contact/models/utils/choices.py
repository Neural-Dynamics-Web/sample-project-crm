# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
# endregion


lead_status_list = [
    ("new", _("New")),
    ("unqualified", _("Unqualified")),
    ("qualified", _("Qualified")),
    ("lost", _("Lost")),
    ("closed_deal", _("Closed Lead")),
    ("open_deal", _("Open Deal"))
]