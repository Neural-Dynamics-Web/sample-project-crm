# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5 import fields as ckeditor
import django
import utils
# endregion

# region				-----Internal Imports-----
from .utils import defaults as local_defaults
# endregion


class Bug(
        utils.models.uuid.UUID
    ):
    # region			    -----Relation-----
    project = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Project"),
        to="development.Project",
        related_name="bugs",
        blank=True,
        null=True
    )

    task = django.db.models.ForeignKey(
        on_delete=django.db.models.CASCADE,
        verbose_name=_("Task"),
        to="development.Task",
        related_name="bugs",
        blank=False,
        null=True
    )
    # endregion

    # region			  -----Informations-----
    description = ckeditor.CKEditor5Field(
        default=local_defaults.description,
        verbose_name=_("Description"),
        config_name="extends",
        blank=False
    )

    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        blank=False,
        null=True
    )
    # endregion
    
    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = _("Bugs")
        verbose_name = _("Bug")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion