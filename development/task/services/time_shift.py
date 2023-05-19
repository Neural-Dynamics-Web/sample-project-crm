# region				-----External Imports-----
import datetime
import django
import utils
# endregion

# region				-----Internal Imports-----
from .. import models as local_models
# endregion


def time_shift(
        task: local_models.Task,
        was: datetime.datetime,
        now: datetime.datetime
    ) -> None:
    if was != now:
        # ? Calculate difference between dates and convert to hours
        difference = round((now - was).total_seconds() / 3600, 2)

        # ? Get all tasks that have delivery end dates
        # ? after the current task actual end date
        tasks = local_models.Task.objects\
            .filter(
                django.db.models.Q(start_date__gte=task.start_date) &
                django.db.models.Q(staff=task.staff) &
                ~django.db.models.Q(id=task.id)
            )\
            .all()
        
        for task in tasks:
            new_date = utils.functions.dates.calculate_end_datetime(
                start_datetime=task.start_date,
                working_time=difference
            )
            
            task.start_date = new_date
            task.save()