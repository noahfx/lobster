import subprocess

from pydub import AudioSegment

def time_range_to_milsec(time_range):
    def time_to_mil(time):
        splitted_time = time.split(":")
        if len(splitted_time) == 2:
            return int(splitted_time[0])*60000 + int(splitted_time[1])*1000
        elif len(splitted_time) == 3:
            return int(splitted_time[0])*360000 + int(splitted_time[1])*60000 \
                + int(splitted_time[2])*1000
    t_range = []
    for t in time_range:
        t_range.append(time_to_mil(t))
    return t_range[0], t_range[1]

def split_audio(src_path, dest_path, split_params, audio_format):
    """
    Splits audio file given the time range in params object
    """
    song = AudioSegment.from_file(src_path, audio_format)
    #first_10 = song[:1000]
    #first_10.export(dest_path, format=audio_format)
    song.export(dest_path, format=audio_format)

def export_format(src_path, dest_path, format='mp3'):
    #TODO implement this ffmpeg -i 1495501084.webm -vn -ab 320k -ar 44100 -y  -f mp3 test.mp3
    pass
