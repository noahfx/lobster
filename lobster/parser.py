from .audio import StreamSegment

def parse_tracks_file(tracks_file):
    """
    Parse tracks file into a list of StreamSegments, each line of the file:
    <track_name>'|'<initial_track_time>
    """
    stream_segs = []
    with open(tracks_file, 'r') as file_:
        for pos, line in enumerate(file_):
            _d = line.split('|')
            stream_segs.append(StreamSegment(name=_d[0], position=pos,
                              initial_time=_d[1], end_time=None))
    return stream_segs
