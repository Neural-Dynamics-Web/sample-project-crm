# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django_ckeditor_5
import django_lifecycle
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import hooks as meeting_notes_hooks
from .utils import choices as local_choices
# endregion


class MeetingNote(
        meeting_notes_hooks.postprocessing.PostprocessingHandlers,
        meeting_notes_hooks.preprocessing.PreprocessingHandlers,
        django_lifecycle.LifecycleModel,
        utils.models.uuid.UUID
    ):
    # region			  -----Informations-----
    audio = django.db.models.FileField(
        validators=[
            utils.models.validators.audio_file_validator
        ],
        verbose_name=_("Audio"),
        upload_to="audio",
        blank=False,
        null=True
    )

    text = django_ckeditor_5.fields.CKEditor5Field(
        verbose_name=_("Text"),
        config_name="extends",
        blank=True,
        null=True
    )

    status = django.db.models.CharField(
        verbose_name=_("Processing Status"),
        choices=local_choices.status_list,
        default="processing_audio",
        max_length=255,
        blank=True
    )

    transcript = django.db.models.TextField(
        verbose_name=_("Transcript"),
        blank=True,
        null=True
    )

    prompt = django.db.models.TextField(
        verbose_name=_("Prompts"),
        blank=False,
        null=True
    )

    title = django.db.models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        blank=True,
        null=True
    )
    # endregion

    # region		    -----Date Calculation-----
    meeting_date = django.db.models.DateField(
        verbose_name=_("Meeting Date"),
        blank=False,
        null=True
    )
    # endregion

    # region			    -----Relation-----
    project = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        related_name="meeting_notes",
        verbose_name=_("Project"),
        to="development.Project",
        blank=True,
        null=True
    )

    deal = django.db.models.ForeignKey(
        on_delete=django.db.models.SET_NULL,
        related_name="meeting_notes",
        verbose_name=_("Deal"),
        to="sales.Deal",
        blank=False,
        null=True
    )
    # endregion

    # region			      -----Metas----
    class Meta(object):
        verbose_name_plural = _("Meeting Notes")
        verbose_name = _("Meeting Note")
    # endregion

    # region			    -----Built-in-----
    def __str__(self) -> str:
        return str(self.title)
    # endregion