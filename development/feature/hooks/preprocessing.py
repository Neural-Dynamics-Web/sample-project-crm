# region				-----External Imports-----
from django.conf import settings
import django_lifecycle
import integrations
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PreprocessingHandlers(object):
    # region			      -----Links----
    # @django_lifecycle.hook(
    #     hook=django_lifecycle.BEFORE_CREATE,
    #     priority=0.010,
    # )
    # def get_information_from_jira(self) -> None:
    #     jira = integrations.jira.api.api.Jira(
    #         email=settings.JIRA_USERNAME,
    #         token=settings.JIRA_TOKEN
    #     )

    #     issue = jira.create_issue(
    #         assignee_id=settings.JIRA_OWNER_ID,
    #         project_id=self.project.jira_id,
    #         parent_key=self.stage.jira_code,
    #         description=self.title,
    #         summary=self.title,
    #         type="Story"
    #     )

    #     self.jira_code = issue["key"]
    #     self.jira_id = issue["id"]

    
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        has_changed=True,
        priority=0.000,
        when="stage"
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.000
    )
    def link_relations(self) -> None:
        self.project = self.stage.project
    # endregion