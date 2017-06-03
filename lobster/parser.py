import re

from .audio import StreamSegment
from .exceptions import InputFileException

def parse_tracks_file(tracks_file):
    """
    Parse tracks file into a list of StreamSegments, each line of the file:
    <track_name>'|'<initial_track_time>
    """
    separator = '|'
    stream_segs = []
    with open(tracks_file, 'r') as file_:
        for pos, line in enumerate(file_):
            if separator not in line:
                raise InputFileException('Input File Error: Missing separator'\
                                         + ' in  line {}'.format(str(pos)))
            _d = line.split(separator)
            validate_line(_d)
            stream_segs.append(StreamSegment(name=_d[0], position=pos,
                              initial_time=_d[1], end_time=None))
    return stream_segs

def validate_line(splitted_line, line_number):
    """
    Validates fomat of every line of the input file
    """
    if len(splitted_line[0]) == 0:
        raise InputFileException('Input File Error: Number of track cannot be'\
                                 + ' empty in line {}'.format(line_number))
    if len(splitted_line[1]) == 0:
        raise InputFileException('Input File Error: Time of the track cannot be'\
                                 + ' empty in line {}'.format(line_number))
    pattern = '([\d]{2}:)?([\d]{2}:[\d]{2})$'
    regex = re.compile(pattern)
    if regex.match(splitted_line[1]) is None:
        raise InputFileException(
            'Input File Error: Wrong format of Time of the'\
            + ' track in line {}'.format((str(line_number))))
    return True
