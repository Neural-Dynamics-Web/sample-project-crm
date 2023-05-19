# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import uuid
# endregion


class UUID(django.db.models.Model):
    # region			      -----Dates----
    id = django.db.models.UUIDField(
        verbose_name=_("ID"),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        abstract = True
    # endregion