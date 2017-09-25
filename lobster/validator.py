import re
from exceptions import(
    InvalidURLException,
    InvalidTrackNumber,
    InvalidTrackTime,
    InvalidSourceType
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

def validate_track_time(time_):
    pattern = '([\d]{2}:)?([\d]{2}:[\d]{2})$'
    regex = re.compile(pattern)
    if regex.match(time_) is None:
        raise InvalidTrackTime
    return time_

def validate_source_type(type_):
    type_ = type_.lower()
    if type_ == 'l':
        return 'local'
    return 'youtube'
