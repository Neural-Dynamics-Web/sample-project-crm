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
    def update_stage_delivery_end_date(self) -> None:
        result = self.stage\
            .calculate_delivery_date_fields(relation="features")
        
        for key, value in result.items(): 
            setattr(self.stage, key, value)
        self.stage.save()


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
    def update_stage_delivery_hours(self) -> None:
        result = self.stage\
            .calculate_delivery_hour_field(relation="features")
        
        for key, value in result.items(): 
            setattr(self.stage, key, value)
        self.stage.save()
    
    
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
    def update_stage_completions(self) -> None:
        result = self.stage\
            .calculate_completion_fields(relation="features")
        
        for key, value in result.items(): 
            setattr(self.stage, key, value)
        self.stage.save()


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
    def update_stage_start_date(self) -> None:
        result = self.stage\
            .calculate_start_date_field(relation="features")
        
        for key, value in result.items(): 
            setattr(self.stage, key, value)
        self.stage.save()


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
    def update_stage_cost(self) -> None:
        result = self.stage\
            .calculate_cost_field(relation="features")
        
        for key, value in result.items(): 
            setattr(self.stage, key, value)
        self.stage.save()
    # endregion