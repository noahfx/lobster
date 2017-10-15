#!/usr/bin/env python
import sys
import argparse


from .audio import create_tracks
from .downloader import YouTube
from .parser import parse_tracks_file
from .prompt import wizard
from .exceptions  import WizardError

def get_from_youtube(source):
    yt = YouTube(source)
    highest_bitrate = yt.audio_available.get('high')
    return yt.download_audio(highest_bitrate)

def get_from_local(source):
    return source

def generate_album(artist, album, tracks, source, input, output,
                   format='mp3', from_wizard=None):
    """
    Generates tracks under dest_dir using the source media file (download|local)
    """
    get_media_file_src = {'youtube': get_from_youtube,
                          'local': get_from_local}
    media_file_src = get_media_file_src.get(source)(input)
    if from_wizard is None:
        audio_segments = parse_tracks_file(tracks)
    else:
        audio_segments = tracks
    create_tracks(media_file_src, output, audio_segments,
                  artist, album, source_type=source, format=format)



def main():
    parser = argparse.ArgumentParser(
        prog='lobster',
        description='Cut audio files with a single command'
    )
    parser.add_argument('--artist', '-ar',  type=str, required=False,
                        help='Name of the artist of the track this will be used '\
                        + 'to name the output directory')
    parser.add_argument('--album', '-al', type=str, required=False,
                        help='Name of the album, this will be used to name '\
                        + 'the output directory')
    parser.add_argument('--tracks', '-t', type=str, required=False,
                        help='File containing the information to build the tracks')
    parser.add_argument('--source', '-s',  type=str, choices=['local', 'youtube'],
                        required=False, help='Name of the media file source')
    parser.add_argument('--input', '-i', type=str, required=False,
                        help='Path to the source media file')
    parser.add_argument('--output', '-o', type=str, required=False,
                        help='Path to the utput directory')
    parser.add_argument('--format', type=str, help='Input media file format',
                        default='mp3')
    mode_help_mesage = 'Launch Lobster in Wizard or Command mode,`wizard`'\
                        ' will launch the Wizard mode, `cmd` will lauch' \
                        ' Command mode, `cmd` is the current default '
    parser.add_argument('--mode', '-m', type=str,
                        help=mode_help_mesage,
                        default='cmd')
    kwargs=vars(parser.parse_args())
    mode = kwargs.get('mode').lower()
    if mode == 'cmd':
        required_fields = ["artist", "album", "tracks", "source", "input",
                           "output"]
        should_generate = True
        for req_field in required_fields:
            if kwargs.get(req_field) is None:
                should_generate = False
                print("Missing required argument --{}".format(req_field))
        if should_generate:
            del kwargs['mode']
            generate_album(**kwargs)
    elif mode == 'wizard':
        try:
            generate_album(**wizard())
        except WizardError:
            sys.exit()
    else:
        print('Invalid {} mode'.format(mode))

sys.exit(main())
