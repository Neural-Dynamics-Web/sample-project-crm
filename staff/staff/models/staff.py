# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
from phonenumber_field import modelfields as phone_fields
from django.contrib.auth.models import AbstractUser
import django
import utils
# endregion

# region				-----Internal Imports-----
from .utils import choices as local_choices
# endregion



class Staff(
        utils.models.uuid.UUID,
        AbstractUser,
    ):
    # region			  -----Informations-----
    type_of_payment = django.db.models.CharField(
        choices=local_choices.type_of_payment_list,
        verbose_name=_("Type Of Payment"),
        max_length=255,
        blank=False,
        null=True
    )
    
    joined_at = django.db.models.DateField(
        verbose_name=_("Joined At"),
        blank=False,
        null=True
    )

    phone = phone_fields.PhoneNumberField(
        verbose_name=_("Phone Number"),
        unique=True,
        blank=False,
        null=True
    )

    linkedin = django.db.models.URLField(
        verbose_name=_("LinkedIn"),
        blank=True,
        null=True
    )

    address = django.db.models.CharField(
        verbose_name=_("Address"),
        max_length=255,
        blank=False, 
        null=True
    )

    email = django.db.models.EmailField(
        verbose_name=_("Email"),
        blank=False,
        null=True
    )

    job = django.db.models.CharField(
        verbose_name=_("Job"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion

    # region			    -----Relation-----
    department = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Department"),
        to="department.Department",
        related_name="staffs",
        blank=True,
        null=True
    )

    country = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        verbose_name=_("Country"),
        related_name="staffs",
        to="geo.Country",
        blank=True,
        null=True
    )
    # endregion

    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Staffs")
        verbose_name = _("Staff")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    # endregion