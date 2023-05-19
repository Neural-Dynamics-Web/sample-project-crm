# region				-----External Imports-----
from django.conf import settings
import django_lifecycle
import integrations
import decimal
import logging
import utils
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
        when_any=[
            "development_hour",
            "start_date"
        ],
        has_changed=True,
        priority=0.013
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.013
    )
    def calculate_development_end_date(self) -> None:
        value = utils.functions.dates.calculate_end_datetime(
            working_time=float(self.development_hour),
            start_datetime=self.start_date
        )
        self.development_end_date = value


    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        when_any=[
            "development_hour",
            "start_date"
        ],
        has_changed=True,
        priority=0.013
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.013
    )
    def calculate_delivery_end_dates(self) -> None:
        value = utils.functions.dates.calculate_end_datetime(
            working_time=float(self.delivery_hour),
            start_datetime=self.start_date
        )

        self.actual_delivery_end_date = value
        self.delivery_end_date = value


    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        when="development_hour",
        has_changed=True,
        priority=0.012
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.012
    )
    def calculate_delivery_hour(self) -> None:
        value = self.development_hour\
              + self.qa_hour

        self.delivery_hour = value


    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        when="development_hour",
        has_changed=True,
        priority=0.011
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.011
    )
    def calculate_qa_hour(self) -> None:
        ratio = settings.TESTING_MULTIPLIER

        value = decimal.Decimal(ratio)\
              * self.development_hour
        
        self.qa_hour = value


    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        when_any=[
            "development_hour",
            "rate"
        ],
        has_changed=True,
        priority=0.020
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.020
    )
    def calculate_cost(self) -> None:
        rate = settings.TESTING_RATE

        _1 = decimal.Decimal(rate)\
           * self.qa_hour
        
        _2 = self.development_hour\
           * self.rate
        
        self.cost = _1 + _2
    # endregion
    
    # region			      -----Links----
    # @django_lifecycle.hook(
    #     hook=django_lifecycle.BEFORE_CREATE,
    #     priority=0.031,
    # )
    # def get_information_from_jira(self) -> None:
    #     jira = integrations.jira.api.api.Jira(
    #         email=settings.JIRA_USERNAME,
    #         token=settings.JIRA_TOKEN
    #     )

    #     issue = jira.create_issue(
    #         assignee_id=settings.JIRA_OWNER_ID,
    #         parent_key=self.feature.jira_code,
    #         project_id=self.project.jira_id,
    #         description=self.title,
    #         summary=self.title,
    #         type="Sub-task"
    #     )

    #     self.jira_code = issue["key"]
    #     self.jira_id = issue["id"]
    
    
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_UPDATE,
        has_changed=True,
        when="feature",
        priority=0.030
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.BEFORE_CREATE,
        priority=0.030
    )
    def link_relations(self) -> None:
        self.project =\
            self.feature.stage.project
        
        self.stage =\
            self.feature.stage
    # endregion

