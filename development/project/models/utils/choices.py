# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
# endregion


current_status_list = [
    ("active_development", _("Active Development")),
    ("supporting", _("Supporting")),
    ("closed_for_good", _("Closed For Good"))
]


sale_status_list = [
    ("lost", _("Lost")),
    ("closed", _("Closed")),
    ("negotiation", _("Negotiation")),
    ("proposal", _("Proposal")),
    ("qualified_to_buy", _("Qualified To Buy")),
    ("new", _("New"))
]


priority_list = [
    ("low", _("Low")),
    ("medium", _("Medium")),
    ("high", _("High"))
]