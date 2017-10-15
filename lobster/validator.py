import re
from exceptions import(
    InvalidURIException,
    InvalidTrackNumber,
    InvalidTrackTime,
    InvalidSourceType
)

def validate_url(url):
    url = url.strip()
    pattern_url = '^(http|https)\:\/\/(([a-zA-Z0-9]|\?|\/|\=|\+|\.|\-))+$'
    pattern_local_file = '^(([\.\/])*([a-zA-Z0-9\-\.\_\~]+))+$'
    regex_url = re.compile(pattern_url)
    regex_local_file = re.compile(pattern_local_file)
    if None in [regex.match(regex_url), regex.match(regex_local_file)]:
        raise InvalidURIException
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
