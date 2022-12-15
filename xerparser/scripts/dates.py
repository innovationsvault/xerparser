from datetime import datetime, timedelta, time


def calc_time_var_hrs(start: time, end: time, ordered: bool = False) -> float:
    """Calculate the variance in hours between two time objects

    Args:
        start (time): start time
        end (time): end time
        ordered (bool, optional): If False, reorder start and end times if start is greater than end. Defaults to False.

    Returns:
        float: Variance between two times in hours
    """

    if not all(isinstance(t, time) for t in [start, end]):
        raise ValueError("Value Error: Arguments must be a time object")

    if not ordered:
        # put dates in proper order so that the smaller date
        # is subtracted from the larger date.
        start, end = min(start, end), max(start, end)

    start_date = datetime.combine(datetime.today(), start)
    end_date = datetime.combine(datetime.today(), end)

    return round((end_date - start_date).total_seconds() / 3600, 2)


def clean_date(date: datetime) -> datetime:
    """Sets time value to 00:00:00 (12AM)"""
    if not isinstance(date, datetime):
        raise ValueError("Value Error: Argument must be a datetime object")

    return date.replace(microsecond=0, second=0, minute=0, hour=0)


def clean_dates(dates: list[datetime]) -> list[datetime]:
    """Remove time values from a list of datetime objects"""
    return [clean_date(d) for d in dates]


def conv_excel_date(ordinal: int, _epoch0=datetime(1899, 12, 31)) -> datetime:
    """Convert Excel date format to datetime object

    Args:
        ordinal (str): Excel date format
        _epoch0 (datetime, optional): Start date for conversion. Defaults to datetime(1899, 12, 31).

    Returns:
        datetime: Excel date format converted to datetime object
    """
    if ordinal < 0 or not isinstance(ordinal, int):
        raise ValueError("Innappropiate value passed, should be positive integer.")

    # Excel leap year bug, 1900 is not a leap year
    if ordinal >= 60:
        ordinal -= 1

    return (_epoch0 + timedelta(days=ordinal)).replace(
        microsecond=0, second=0, minute=0, hour=0
    )


def conv_time(time_str: str) -> time:
    """Convert a string representing time into a datetime.time object.

    Args:
        time_str (str): time as string

    Returns:
        time: time as datetime.time object
    """
    return datetime.strptime(time_str, "%H:%M").time()


def date_variance_days(dt1: datetime, dt2: datetime) -> int | None:
    """Calculate variance in days between two dates."""
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        return

    return (dt1 - dt2).days


def date_to_str(date, include_weekday: bool = False) -> str:
    """Convert datetime object to string."""
    if date is None:
        return "-"

    if not isinstance(date, datetime):
        raise ValueError("Expected datetime object")

    date_format = ("%d-%b-%Y", "%a %d-%b-%Y")[include_weekday]

    return datetime.strftime(date, date_format)