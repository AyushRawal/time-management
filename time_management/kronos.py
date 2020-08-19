from datetime import datetime
from datetime import timedelta

string_format_time = "%Y-%m-%d %H:%M:%S"

week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_date_time_as_string():
    return get_date_time().strftime(string_format_time)


def get_date_time_from_string(date_time_str):
    return datetime.strptime(date_time_str, string_format_time)


def get_date_time():
    return datetime.now()


def is_previous_friday(date_time_string, today=get_date_time()):
    date_time = get_date_time_from_string(date_time_string)
    pre_friday = today - timedelta(days=3)
    return date_time.date() == pre_friday.date()


def is_yesterday(date_time_string, today=get_date_time()):
    date_time = get_date_time_from_string(date_time_string)
    yesterday = today - timedelta(days=1)
    return date_time.date() == yesterday.date()


def get_day_of_week(date_time):
    return week_days.get(date_time.weekday())


def is_overdue(date_time_string, completion_goal):
    date_time = get_date_time_from_string(date_time_string)
    completion_goal = float(completion_goal)
    return (date_time + timedelta(days=completion_goal)) < datetime.now()
