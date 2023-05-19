# region				-----External Imports-----
import django_lifecycle
import django
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
            "actual_delivery_end_date",
            "delivery_end_date"
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
    def update_feature_delivery_end_date(self) -> None:
        result = self.feature\
            .calculate_delivery_date_fields(relation="tasks")
        
        for key, value in result.items(): 
            setattr(self.feature, key, value)
        self.feature.save()


    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        when="delivery_hour",
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
    def update_feature_delivery_hours(self) -> None:
        result = self.feature\
            .calculate_delivery_hour_field(relation="tasks")
        
        for key, value in result.items(): 
            setattr(self.feature, key, value)
        self.feature.save()


    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        when="start_date",
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
    def update_feature_start_date(self) -> None:
        result = self.feature\
            .calculate_start_date_field(relation="tasks")
        
        for key, value in result.items(): 
            setattr(self.feature, key, value)
        self.feature.save()


    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        has_changed=True,
        priority=0.010,
        when="cost"
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_DELETE,
        priority=0.010
    )
    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_CREATE,
        priority=0.010
    )
    def update_feature_cost(self) -> None:
        result = self.feature\
            .calculate_cost_field(relation="tasks")
        
        for key, value in result.items(): 
            setattr(self.feature, key, value)
        self.feature.save()


    @django_lifecycle.hook(
        hook=django_lifecycle.AFTER_UPDATE,
        when_any=[
            "qa_status",
            "status"
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
    def update_feature_completion(self) -> None:
        aggregations = {
            "development": django.db.models.Count(
                filter=django.db.models.Q(
                    tasks__status="completed"
                ),
                expression="tasks"
            ),
            "delivery": django.db.models.Count(
                filter=django.db.models.Q(
                    tasks__qa_status="passed"
                ),
                expression="tasks"
            ),
            "all": django.db.models.Count(
                expression="tasks"
            )
        }

        result = self.feature.__class__\
            .objects.filter(id=self.feature.id)\
            .prefetch_related("tasks")\
            .aggregate(**aggregations)
        
        try:
            development = result["development"]\
                        / result["all"]\
                        * 100
        except ZeroDivisionError:
            development = 0
        
        try:
            delivery = result["delivery"]\
                     / result["all"]\
                     * 100

        except ZeroDivisionError:
            delivery = 0
        
        result = {
            "development_completion": development,
            "delivery_completion": delivery
        }
        
        for key, value in result.items(): 
            setattr(self.feature, key, value)
        self.feature.save()
    # endregion