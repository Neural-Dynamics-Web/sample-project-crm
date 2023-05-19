# region				-----External Imports-----
import django_lifecycle
import development
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PreprocessingHandlers(object):
    # region			  -----Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        has_changed=True,
        priority=0.000,
        when="status",
        is_now="win"
    )
    def generate_stage(self) -> None:
        stage = development.models.Stage\
            .objects.create(
                project=self.project,
                title=self.title
            )
        
        self.stage = stage
    # endregion