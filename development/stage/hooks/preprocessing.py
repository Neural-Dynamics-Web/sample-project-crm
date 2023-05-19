# region				-----External Imports-----
from django.conf import settings
import django_lifecycle
import integrations
import decimal
import logging
# endregion

# region				-----Internal Imports-----
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


class PreprocessingHandlers(object):
    # region		  -----Similar Calculations-----
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        has_changed=True,
        priority=0.000,
        when="cost"
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_DELETE,
        priority=0.000
    )
    def update_stage_costs_range(self) -> None:
        ratio = settings.PROJECT_MANAGEMENT_MULTIPLIER
        ratio = decimal.Decimal(ratio)

        rate = settings.PROJECT_MANAGEMENT_RATE
        rate = decimal.Decimal(rate)

        _1 = self.delivery_hour\
           * ratio\
           * rate

        self.cost += _1
    

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
    #         description=self.title,
    #         summary=self.title,
    #         type="Epic"
    #     )

    #     self.jira_code = issue["key"]
    #     self.jira_id = issue["id"]
    # endregion