#!/usr/bin/env python
import sys
import argparse

import lobster

from lobster.audio import create_tracks
from lobster.downloader import YouTube
from lobster.parser import parse_tracks_file
from lobster.prompt import wizard

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
    parser = argparse.ArgumentParser(description='Cut audio files with a single command')
    parser.add_argument('--artist', '-ar',  type=str, required=True,
                        help='Name of the artist of the track this will be used '\
                        + 'to name the output directory')
    parser.add_argument('--album', '-al', type=str, required=True,
                        help='Name of the album, this will be used to name '\
                        + 'the output directory')
    parser.add_argument('--tracks', '-t', type=str, required=True,
                        help='File containing the information to build the tracks')
    parser.add_argument('--source', '-s',  type=str, choices=['local', 'youtube'],
                        required=True, help='Name of the media file source')
    parser.add_argument('--input', '-i', type=str, required=True,
                        help='Path to the source media file')
    parser.add_argument('--output', '-o', type=str, required=True,
                        help='Path to the utput directory')
    parser.add_argument('--format', type=str, help='Input media file format',
                        default='mp3')
    kwargs=vars(parser.parse_args())

    if kwargs.get('wizard') is None:
        generate_album(**kwargs)
    else:
        generate_album(**wizard())

sys.exit(main())
