from datetime import datetime

import pytz

from const.constant import DATE_FORMAT


def date_converter(db_datetime):
    datetime_utc = datetime.strptime(db_datetime, DATE_FORMAT)
    datetime_utc = datetime_utc.replace(tzinfo = pytz.UTC)
    local_datetime = datetime_utc.astimezone()

    return local_datetime.strftime(DATE_FORMAT)
