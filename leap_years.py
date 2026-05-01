def is_leap_year(year: int) -> bool:
    """Returns True if the supplied year is a leap year, False otherwise"""
    if year % 4 == 0:
        return year % 100 != 0
    return False