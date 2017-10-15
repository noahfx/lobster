URL_MESSAGE = ' Enter Video URL: '
TRACKS_NUMBER_MESSAGE = ' Enter Number of tracks: '
TRACK_NAME_MESSAGE = ' Enter Track Number {} Name: '
TRACK_INIT_MESSAGE = ' Enter Time where Track {} starts: (e.g: 04:20) '
OUTPUT_DIRECTORY_MESSAGE = ' Enter the destination directory: '
SOURCE_MESSAGE = ' Enter source file path: '
SOURCE_TYPE_MESSAGE = ' Enter the source y=Youtube|l=local: [Y/l] '
CONFIRMATION_MESSAGE = ' Is the above information ok? [Y:n] '
ALBUM_NAME_MESSAGE = ' Enter album name: '
ARTIST_NAME_MESSAGE = ' Enter artist name: '

TRACK_NAME_ERROR = ' Error: Invalid Track Name'
TRACKS_NUMBER_ERROR = ' Error: Invalid Number of Tracks'
URL_MESSAGE_ERROR = ' Error: Invalid URI'
TRACK_TIME_MESSAGE_ERROR = ' Error: Invalid format for track time'
SOURCE_TYPE_ERROR = ' Error: Invalid Source Type'
ALBUM_NAME_MESSAGE_ERROR = ' Invalid album name '
ARTIST_NAME_MESSAGE_ERROR = ' Invalid artist name '

def generate_confirmation_message(data):
    """
    Generates confirmation message showing all data
    retrieved from wizard
    """

    _data0 = 'artist: %(artist)s \n album: %(album)s \n source: %(source)s \n' \
             ' input: %(input)s \n output: %(output)s' % data
    _data1 = ' tracks: \n'
    for track in data.get('tracks'):
        _data1 = '{} {} \n{}\n'.format(_data1, str(track), 15*'-')

    _data2 = 'Is the above information correct: [Y/n]'
    return '\n information:\n {}\n{}\n{}'.format(_data0, _data1, _data2)
