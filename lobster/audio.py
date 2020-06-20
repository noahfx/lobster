import subprocess

from pydub import AudioSegment
from .filemanager import get_workingdir, get_album_dir

class StreamSegment(object):
    def __init__(self, name, position, initial_time=None, end_time=None):
        self.name = name
        self.position = position
        self.initial_time = initial_time
        self.end_time = end_time
        self.orig_tmp_file = None

    def __str__(self):
        return "name: {} \n poisition: {} \n initial time: {} \n".format(
            self.name,
            str(self.position),
            str(self.initial_time)
        )

def time_to_mil(time):
    splitted_time = time.split(":")
    if len(splitted_time) == 2:
        return int(splitted_time[0])*60000 + int(splitted_time[1])*1000
    elif len(splitted_time) == 3:
        return int(splitted_time[0])*360000 + int(splitted_time[1])*60000 \
            + int(splitted_time[2])*1000

def build_time_range(stream_len, streamSegments):
    """
    Sets initial time/end time for segments
    """
    t_separator = 500 #separator between track, milseconds
    sortedStreamSegments = sorted(streamSegments, key=lambda ss: ss.position)
    for idx, stream_segment in enumerate(sortedStreamSegments):
        stream_segment.initial_time = time_to_mil(stream_segment.initial_time)
        if stream_segment.position == 0:
            if stream_segment.end_time is None:
                if len(streamSegments) == 1:
                    stream_segment.end_time = stream_len - t_separator
                else:
                    nxt_stream_init_t = sortedStreamSegments[idx + 1].initial_time
                    stream_segment.end_time = time_to_mil(nxt_stream_init_t) - t_separator
        elif stream_segment.position < len(streamSegments) - 1:
            if stream_segment.end_time is None:
                nxt_stream_init_t = sortedStreamSegments[idx + 1].initial_time
                stream_segment.end_time = time_to_mil(nxt_stream_init_t) - t_separator
        else:
            if stream_segment.end_time is None:
                stream_segment.end_time = stream_len - t_separator
    return sortedStreamSegments

def split_audio(src_file, dest_path, audio_segments, audio_format='webm'):
    """
    Splits audio file given the time range in audio segments
    """
    audio_orig = AudioSegment.from_file(src_file, 'webm')
    print('Preparing audio, this may take a while... go for coffee')
    s_audio_segments = build_time_range(len(audio_orig), audio_segments)
    for as_ in audio_segments:
        tmp_seg = audio_orig[int(as_.initial_time):int(as_.end_time)]
        file_name = as_.name.replace(' ', '') + '.' + audio_format
        as_.orig_tmp_file = '/'.join([dest_path, file_name])
        tmp_seg.export(as_.orig_tmp_file, format=audio_format)
    return audio_segments

def export(src_file, dest_file, track_metadata=None, format='mp3'):
    """
    Exports webm file to mp3 or ogg format file, replaces pydub export
    due to issues with ffmpeg
    """
    print('Exporting audio to {}'.format(dest_file))
    ffmpeg_cmd = ['ffmpeg', '-i', src_file, '-vn', '-ab', '320k', '-ar',
                  '44100']
    cmd_last = ['-y', dest_file ]
    if track_metadata is not None:
        ffmpeg_cmd = ffmpeg_cmd + track_metadata + cmd_last
    else:
        ffmpeg_cmd = ffmpeg_cmd + cmd_last
    p = subprocess.Popen(ffmpeg_cmd,  stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        print(err)
        raise Exception("Could not encode file")
    return dest_file

def create_tracks(source_media, dest_dir, audio_segments, artist, album,
                  source_type, format='mp3'):
    src_format = format
    if source_type == 'youtube':
        src_format = 'webm'
    dir_name = '_'.join([artist.replace(' ', '_'), album.replace(' ', '_')])
    dest_dir = '/'.join([dest_dir, dir_name])
    print(dest_dir)
    print(format)
    dest_file = lambda name: '/'.join([dest_dir ,name.replace(' ', '_') + '.' +\
                                       format])
    splitted_segments = split_audio(source_media, get_workingdir(),
                                    audio_segments, audio_format=src_format)
    album_dir = get_album_dir(dest_dir)
    print("Created {}".format(album_dir))
    for as_ in splitted_segments:
        track_meta = _create_track_metadata(album, artist,
                                            as_.name, as_.position + 1)
        export(as_.orig_tmp_file, dest_file(as_.name),
               track_metadata=track_meta, format=format)

def _create_track_metadata(album, artist, name, track_number):
    return ['-metadata', '='.join(['title', name]),
            '-metadata', '='.join(['album_artist', artist]),
            '-metadata', '='.join(['artist', artist]),
            '-metadata', '='.join(['album', album]),
            '-metadata', '='.join(['track', str(track_number)])]
