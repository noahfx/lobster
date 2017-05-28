from audio import create_tracks
from downloader import YouTube
from parser import parse_tracks_file

def get_from_youtube(source):
    yt = YouTube(source)
    highest_bitrate = yt.audio_available.get('high')
    return yt.download_audio(highest_bitrate)

def get_from_local(source):
    return source

def generate_album(artist, album, tracks_file, type_, source, dest_dir,
                   format='mp3'):
    """
    Generates tracks under dest_dir using the source media file (download|local)
    """
    get_media_file_src = {'youtube': get_from_youtube,
                          'local': get_from_local}
    media_file_src = get_media_file_src.get(type_)(source)
    audio_segments = parse_tracks_file(tracks_file)
    create_tracks(media_file_src, dest_dir, audio_segments,
                  artist, album, source_type=source, format=format)


if __name__ == '__main__':
    generate_album('Cybernetic Witchcult', 'Spaceous Cretaceous',
                   '/tmp/tracks', 'youtube', 'https://www.youtube.com/watch?v=I_X4xJ29DOQ',
                   '/tmp')
