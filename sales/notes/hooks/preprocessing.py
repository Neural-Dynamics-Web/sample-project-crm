# region				-----External Imports-----
import django_lifecycle
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
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.010,
    )
    def generate_title(self) -> None:
        date = self.meeting_date.strftime("%d/%m/%Y")
        self.title = "{project} {date}".format(
            project=self.project.title,
            date=date
        )
    
    
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.000,
    )
    def link_relations(self) -> None:
        self.project = self.deal.project
    # endregion