# region				-----External Imports-----
from django.conf import settings
import datetime
import typing
import pytz
# endregion


def calculate_end_datetime(
        start_datetime: datetime.datetime,
        working_time: int
    ) -> datetime.datetime:
    # ? Function to convert seconds in duration to normal hours
    to_minutes = lambda duration: round(duration.total_seconds() / 60, 2)

    # ? Generate lower and upper limit of tipical working day
    lower_datetime, upper_datetime = get_lower_and_upper_limit(
        start_datetime=start_datetime
    )
    
    # ? Calculate rest of working hours using working hours
    if working_time > 0:
        free_today = to_minutes(upper_datetime - start_datetime)
    else:
        free_today = to_minutes(start_datetime - lower_datetime)
    
    working_time = working_time * 60

    # ? Initialize start date and end date respectively
    start_datetime, end_datetime =\
        start_datetime, start_datetime

    if abs(working_time) >= free_today:
        delta = abs(working_time) - free_today
        if delta >= 480:
            tail = delta - (delta // 480) * 480
            days = delta // 480

            if working_time > 0:
                end_datetime = lower_datetime\
                             + datetime.timedelta(days=days + 1)\
                             + datetime.timedelta(minutes=tail)
            else:
                end_datetime = upper_datetime\
                             - datetime.timedelta(days=days + 1)\
                             - datetime.timedelta(minutes=tail)
        else:
            if working_time > 0:
                end_datetime = lower_datetime\
                             + datetime.timedelta(minutes=delta)\
                             + datetime.timedelta(days=1)
            else:
                end_datetime = upper_datetime\
                             - datetime.timedelta(minutes=delta)\
                             - datetime.timedelta(days=1)
    else:
        end_datetime += datetime.timedelta(
            minutes=working_time
        )
    
    # ? Count how many weekends were in
    # ? our start and end dates
    weekends_passed = weekends_in_range(
        start_datetime=start_datetime, 
        end_datetime=end_datetime
    )

    # ? If there were any weekends then
    # ? increment end date by formula
    if weekends_passed:
        if working_time > 0:
            end_datetime += datetime.timedelta(
                days=weekends_passed
            )
        else:
            end_datetime -= datetime.timedelta(
                days=weekends_passed
            )
    
    return end_datetime


def get_lower_and_upper_limit(
        start_datetime: datetime.datetime
    ) -> typing.Tuple[datetime.datetime]:
    upper_datetime = datetime.datetime.combine(
        start_datetime.date(), datetime.time(20, 0, 0)
    )

    upper_datetime = pytz.timezone(settings.TIME_ZONE)\
        .localize(upper_datetime)
    
    lower_datetime = datetime.datetime.combine(
        start_datetime.date(), datetime.time(12, 0, 0)
    )

    lower_datetime = pytz.timezone(settings.TIME_ZONE)\
        .localize(lower_datetime)
    
    return lower_datetime, upper_datetime


def weekends_in_range(
        start_datetime: datetime.datetime,
        end_datetime: datetime.datetime
    ) -> int:
    weekends_counter = 0

    if start_datetime < end_datetime:
        days = (end_datetime - start_datetime).days + 1
    else:
        days = (start_datetime - end_datetime).days + 1

    # ? Decide where to go: forward or backward
    if start_datetime < end_datetime:
        for day in range(days):
            current_date = start_datetime\
                         + datetime.timedelta(days=day)

            if current_date.weekday() == 5:
                    weekends_counter += 2
    else:
        for day in range(days):
            current_date = start_datetime\
                         - datetime.timedelta(days=day)
                
            if current_date.weekday() == 6:
                weekends_counter += 2
    
    if days == 1:
        if end_datetime.weekday() in [5, 6]:
            weekends_counter += 2

    
    return weekends_counter


def working_day():
    lower_date = datetime.datetime.combine(
        datetime.datetime.now().today(),
        datetime.time(12, 0, 0)
    )
    return lower_date


def midnight():
    pass