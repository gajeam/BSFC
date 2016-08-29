import pytz
from .constants import PACIFIC_TIMEZONE


def convert_utc_to_pacific(utc_datetime):
    pacific_timezone = pytz.timezone(PACIFIC_TIMEZONE)
    return pacific_timezone.normalize(utc_datetime)


def convert_pacific_to_utc(local_datetime):
    return local_datetime.astimezone(pytz.utc)