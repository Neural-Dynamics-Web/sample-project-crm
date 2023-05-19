# region				-----External Imports-----
import django_lifecycle
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PostprocessingHandlers(object):
    # region		  -----Similar Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        when_any=[
            "development_completion",
            "delivery_completion"
        ],
        has_changed=True,
        priority=0.000
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_DELETE,
        priority=0.000
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_CREATE,
        priority=0.000
    )
    def update_project_completions(self) -> None:
        result = self.project\
            .calculate_completion_fields(relation="stages")
        
        for key, value in result.items(): 
            setattr(self.project, key, value)
        self.project.save()
    # endregion