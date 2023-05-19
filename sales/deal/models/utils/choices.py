# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
# endregion


status_list = [
    ("first_contact", _("First Contact")),
    ("discovery", _("Discovery")),
    ("evaluation", _("Evaluation")),
    ("document_signing", _("Document Signing")),
    ("win", _("Win")),
    ("lose", _("Lose"))
]

development_status_list = [
    ("rated", _("Rated")),
    ("started", _("Started")),
    ("completed", _("Completed"))
]