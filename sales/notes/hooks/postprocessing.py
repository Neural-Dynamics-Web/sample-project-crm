# region				-----External Imports-----
import django_lifecycle
import celery
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PostprocessingHandlers(object):
    # region			  -----Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        priority=0.000,
        is_now="error",
        when="status",
        was="error"
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_CREATE,
        priority=0.000
    )
    def process_audio(self) -> None:
        celery.current_app.send_task(
            name="process_meeting_note",
            kwargs={
                "meeting_note_id": self.id
            }
        )
    # endregion