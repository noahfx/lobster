import sys
import time
import readline

#from audio import StreamSegment
from prompt_messages import *
from exceptions import *
from validator import validate_url, validate_track_number


def prompt_print(message, direction='STDOUT', color=None):
    """
    Prints to prompt stdout 
    """
    def _print(message_):
        return '<lobster> {}'.format(message_)

    paint_red = lambda msg : '\033[01;31m{}\033[00m'.format(msg)
    paint_green = lambda msg : '\033[1;36m{}\033[00m'.format(msg)
    paint_white = lambda msg : msg
    paint = {
        "GREEN" : paint_green,
        "RED" : paint_red,
        "WHITE" : paint_white
    }

    if color is None:
        color = "WHITE"

    if direction == 'STDOUT':
        sys.stdout.write(_print(paint.get(color)(message)))
        sys.stdout.write("\n")
    elif direction == 'STDIN':
        return input(_print(paint.get(color)(message)))

def get_clam():
    return ' (\/) (°,,,°) (\/) -- woop woop woop'

def wizard():
    input_data = dict(segments=[])
    prompt_print(get_clam(), color='RED', direction='STDOUT')
    try: 
        input_data['url'] = validate_url(prompt_print(
            URL_MESSAGE,
            direction='STDIN'
        ))
        input_data['track_number'] = validate_track_number(prompt_print(
            TRACKS_NUMBER_MESSAGE,
            direction='STDIN'
        ))

        for i in range(0, input_data.get('track_number')):
            _number = str(i + 1)
            name = prompt_print(TRACK_NAME.format(_number), direction='STDIN')
            init_time = prompt_print(TRACK_INIT.format(_number), direction= 'STDIN')
            """"input_data.get('segments').append(StreamSegment(
                name=name,
                position=i,
                initial_time=init_time
            ))"""
        
    except InvalidURLException:
        input_data['url'] = validate_url(prompt_print(URL_MESSAGE_ERROR,
                                                      direction='STDIN'))
    except InvalidTrackNumber:
        input_data['track_number'] = validate_track_number(prompt_print(TRACKS_NUMBER_ERROR),
                                                           direction='STDIN')
        

wizard()


