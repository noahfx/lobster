import re
from exceptions import(
    InvalidURLException,
    InvalidTrackNumber
)

def validate_url(url):
    pattern = '(http|https)\:\/\/(([a-zA-Z0-9]|\?|\/|\=|\+|\.|\-))+$'
    regex = re.compile(pattern)
    if regex.match(url) is None:
        raise InvalidURLException
    return url

def validate_track_number(number):
    try:
        value = int(number)
        if value < 1:
            raise InvalidTrackNumber
        return value
    except ValueError:
        raise InvalidTrackNumber

