# region				-----External Imports-----
from django.conf import settings
import datetime
import decimal
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import models as local_models
# endregion


class TaskForm(django.forms.ModelForm):
    start_date = django.forms.SplitDateTimeField(
        widget=utils.widgets.datetime.CustomSplitDateTime(),
        initial=django.utils.timezone.now()
    )
    

    def clean(self) -> None:
        development_hours = self.cleaned_data.get("development_hour")
        start_datetime = self.cleaned_data.get("start_date")

        if start_datetime and development_hours:
            if self.Meta.model.objects.filter(id=self.instance.id).first():
                delivery_end_datetime = self.instance.actual_delivery_end_date
            else:
                delivery_end_datetime = self.__calculate_delivery_end_date(
                    start_datetime=start_datetime,
                    hours=development_hours
                )

            # ? Start validation from very basic validation checks
            if datetime.datetime.now().date() > start_datetime.date():
                raise django.core.exceptions.ValidationError(
                    {"start_date": "It is retroactive datetime"}
                )

            if start_datetime.hour <= 11 or start_datetime.hour >= 20:
                raise django.core.exceptions.ValidationError(
                    {"start_date": "It is refreshment hours"}
                )
            
            if start_datetime.weekday() in [5, 6]:
                raise django.core.exceptions.ValidationError(
                    {"start_date": "It is weekends"}
                )
            
            if development_hours >= 24:
                raise django.core.exceptions.ValidationError(
                    {"development_hour": "Too long"}
                )
            
            start_datetime = self.cleaned_data.get("start_date")
            staff = self.cleaned_data.get("staff")

            task = {
                "actual_delivery_end_date": delivery_end_datetime,
                "start_date": start_datetime,
            }
            
            overlap_condition = django.db.models.Q(
                django.db.models.Q(
                    actual_delivery_end_date__date__lte=(
                        start_datetime + datetime.timedelta(days=4)
                    ).date()
                ) &
                django.db.models.Q(
                    start_date__date__gte=(
                        start_datetime - datetime.timedelta(days=4)
                    ).date()
                ) &
                django.db.models.Q(staff=staff)
            )
            
            overlaped_tasks = local_models.Task.objects\
                .filter(overlap_condition)
            
            if self.instance.id:
                overlaped_tasks = overlaped_tasks\
                    .exclude(id=self.instance.id)

            overlaped_tasks = overlaped_tasks\
                .values(
                    "actual_delivery_end_date", 
                    "start_date"
                ).order_by(
                    "start_date"
                )
            
            
            # ? If not overlaped tasks exist 
            # ? then just let skip checks
            if not overlaped_tasks:
                return

            # ? Check if start date does not
            # ? overlaps start or end
            for date in overlaped_tasks:
                if (
                    (
                        date["start_date"] <= 
                        task["actual_delivery_end_date"] <= 
                        date["actual_delivery_end_date"]
                    )
                    or
                    (
                        date["start_date"] <= 
                        task["start_date"] <= 
                        date["actual_delivery_end_date"]
                    )
                ):
                    raise django.core.exceptions.ValidationError(
                        {"start_date": "Some task is running at this time"}
                    )
                elif (
                    (
                        task["start_date"] <= 
                        date["actual_delivery_end_date"] <= 
                        task["actual_delivery_end_date"]
                    )
                    or
                    (
                        task["start_date"] <= 
                        date["start_date"] <= 
                        task["actual_delivery_end_date"]
                    )
                ):
                    raise django.core.exceptions.ValidationError(
                        {"start_date": "Some task is running at this time"}
                    )
                elif (
                    (
                        date["actual_delivery_end_date"] <= 
                        task["actual_delivery_end_date"]
                    )
                    and
                    (
                        date["start_date"] >= 
                        task["start_date"]
                    )
                ):
                    raise django.core.exceptions.ValidationError(
                        {"start_date": "Some task is running at this time"}
                    )
    

    def __calculate_delivery_end_date(self,
            start_datetime: datetime.datetime,
            hours: float    
        ) -> datetime.datetime:
        coefficient = decimal.Decimal(settings.TESTING_MULTIPLIER)
        
        value = utils.functions.dates.calculate_end_datetime(
            working_time=float(hours + hours * coefficient),
            start_datetime=start_datetime
        )
        return value
    

    class Meta(object):
        model = local_models.Task
        fields = "__all__"