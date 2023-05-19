# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
from phonenumber_field import modelfields as phone_fields
import django
import utils
# endregion

# region				-----Internal Imports-----
from .utils import choices as local_choices
# endregion


class Contact(
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    lead_status = django.db.models.CharField(
        choices=local_choices.lead_status_list,
        verbose_name=_("Lead Status"),
        max_length=255,
        default="new",
        blank=False
    )

    phone = phone_fields.PhoneNumberField(
        verbose_name=_("Phone Number"),
        unique=True,
        blank=True,
        null=True
    )

    position = django.db.models.CharField(
        verbose_name=_("Position"),
        max_length=255,
        blank=False,
        null=True
    )

    telegram = django.db.models.CharField(
        verbose_name=_("Telegram"),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    company = django.db.models.CharField(
        verbose_name=_("Company"),
        max_length=255,
        blank=False,
        null=True
    )

    email = django.db.models.EmailField(
        verbose_name=_("Email"),
        unique=True,
        blank=True,
        null=True
    )

    name = django.db.models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion
    
    # region			    -----Relation-----
    projects = django.db.models.ManyToManyField(
        verbose_name=_("Projects"),
        to="development.Project",
        related_name="contacts",
        blank=True
    )

    country = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Country"),
        related_name="contacts",
        to="geo.Country",
        blank=False,
        null=True
    )

    source = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Source"),
        related_name="contacts",
        to="sales.Source",
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Dates----
    last_call = django.db.models.DateField(
        verbose_name=_("Last Call"),
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Contacts")
        verbose_name = _("Contact")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return f"{self.name}"
    # endregion