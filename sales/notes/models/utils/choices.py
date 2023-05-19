# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
# endregion


status_list = [
    ("processing_transcript", _("Processing Transcript")),
    ("processing_audio", _("Processing Audio")),
    ("processed", _("Processed")),
    ("error", _("Error"))
]