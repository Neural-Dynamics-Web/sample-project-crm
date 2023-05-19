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
    # @django_lifecycle.hook(
    #     hook=django_lifecycle.BEFORE_CREATE,
    #     priority=0.000,
    # )
    # def get_information_from_jira(self) -> None:
    #     jira = integrations.jira.api.api.Jira(
    #         email=settings.JIRA_USERNAME,
    #         token=settings.JIRA_TOKEN
    #     )

    #     project = jira.get_project(
    #         key=self.jira_code
    #     )

    #     self.jira_id = project["id"]
    pass