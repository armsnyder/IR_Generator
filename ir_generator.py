__author__ = 'Adam Snyder'

import wave
import struct
import sys
import librosa

def main():
    if len(sys.argv) != 3:
        print "usage: ir_generator.py [wet_audio] [dry_audio]"
        return
    wet_audio = get_wav_array(sys.argv[1])
    dry_audio = get_wav_array(sys.argv[2])
    impulse_response = make_impulse(wet_audio, dry_audio)


def get_wav_array(filename):
    """
    Reads a wav file into an array
    :param filename: wav file
    :return: array, sample rate
    """
    p = wave.open(filename, 'r')
    n_channels, sample_width, sample_rate, n_frames, comp_type, comp_name = p.getparams()
    frames = p.readframes(n_frames * n_channels)
    return struct.unpack_from("%dh" % n_frames * n_channels, frames), sample_rate


def make_impulse(wet_audio, dry_audio):
    return 0

if __name__ == '__main__':
    main()
