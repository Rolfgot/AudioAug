import scipy
import argparse
import soundfile as sf
import numpy as np

from aug_wav import AugWav

parser = argparse.ArgumentParser()
parser.add_argument('--config_path', type=str, default="config.yml", help='path to config file yaml')
parser.add_argument('--file_path', type=str, default="test.wav", help='input wav file')
args = parser.parse_args()
config_path = args.config_path
file_path = args.file_path

augwav = AugWav()
data, sr = sf.read(file_path)
# sr, data = scipy.io.wavfile.read(file_path)
data = data.T

augwav.aug_all(data)
if augwav.aug_loud_out is not None:
    # scipy.io.wavfile.write(file_path[:-4] + "_loud.wav", sr, augwav.aug_loud_out.T)
    sf.write(file_path[:-4] + "_loud.wav", np.ravel(augwav.aug_loud_out.T), int(2*sr))
if augwav.aug_noise_out is not None:
    # scipy.io.wavfile.write(file_path[:-4] + "_noise.wav", sr, augwav.aug_noise_out.T)
    sf.write(file_path[:-4] + "_noise.wav", np.ravel(augwav.aug_noise_out.T), int(2*sr))
if augwav.aug_shift_out is not None:
    # scipy.io.wavfile.write(file_path[:-4] + "_shift.wav", sr, augwav.aug_shift_out.T)
    sf.write(file_path[:-4] + "_shift.wav", np.ravel(augwav.aug_shift_out.T), int(2*sr))
if augwav.aug_speed_out is not None:
    # scipy.io.wavfile.write(file_path[:-4] + "_speed.wav", sr, augwav.aug_speed_out.T)
    sf.write(file_path[:-4] + "_speed.wav", np.ravel(augwav.aug_speed_out.T), int(2*sr))
