import subprocess

from pydub import AudioSegment

class StreamSegment(object):
    def __init__(self, name, position, initial_time=None, end_time=None):
        self.name = name
        self.position = position
        self.initial_time = initial_time
        self.end_time = end_time
        self.orig_tmp_file = None

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
    sortedStreamSegments = sort(streamSegments, key=lambda ss: ss.position)
    for idx, stream_segment in enumerate(sortedStreamSegments):
        if stream_segment.position == 0:
            stream_segment.initial_time = 0
            if stream_segment.end_time is None:
                stream_segment.end_time = time_to_mil(nxt_stream_init_t) - t_separator
        elif stream_segment.position != len(stream_segment) - 1:
            if stream_segment.end_time is None:
                nxt_stream_init_t = sortedStreamSegments[idx + 1].initial_time
                stream_segment.end_time = time_to_mil(nxt_stream_init_t) - t_separator
        else:
            if stream_segment.end_time is None:
                stream_segment.end_time = stream_len - time_separator
    return sortedStreamSegments

def split_audio(src_path, dest_path, split_params, audio_format):
    """
    Splits audio file given the time range in params object
    """
    song = AudioSegment.from_file(src_path, audio_format)
    #first_10 = song[:1000]
    #first_10.export(dest_path, format=audio_format)
    song.export(dest_path, format=audio_format)

def export(src_file, dest_file, format='mp3'):
    """
    Exports webm file to mp3 or ogg format file, replaces pydub export
    due to issues with ffmpeg
    """
    ffmpeg_cmd = ['ffmpeg', '-i', src_file, '-vn', '-ab', '320k', 'ar', '44100',
                  '-y', dest_file ]
    p = subprocess.Popen(ffmpeg_cmd,  stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception("Could not encode file")
    return dest_file
