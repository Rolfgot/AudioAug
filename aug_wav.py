import numpy as np
import yaml
from scipy.fft import fft, irfft


class AugWav():
    def __init__(self):
        self.do_aug_loud = True
        self.do_aug_noise = True
        self.do_aug_shift = True
        self.do_aug_speed = True

        self.loudness_level = 0.5
        self.noise_factor = 0.009
        self.sample_rate = 48000
        self.shift_max = 0.2
        self.shift_direction = 'both'
        self.speed_factor = 0.5

        self.aug_loud_out = None
        self.aug_noise_out = None
        self.aug_shift_out = None
        self.aug_speed_out = None

    def get_config(self, config_path):
        data_yaml = yaml.safe_load(open(config_path))
        do_aug_loud = data_yaml["do_aug_loud"]
        loudness_levdo_aug_noiseata_yaml["do_aug_noise"]
        do_aug_shift = data_yaml["do_aug_shift"]
        do_aug_speed = data_yaml["do_aug_speed"]
        loudness_level = data_yaml["loudness_level"]
        noise_factor = data_yaml["noise_factor"]
        sample_rate = data_yaml["sample_rate"]
        shift_max = data_yaml["shift_max"]
        output_method = data_yaml["output_method"]
        shift_direction = data_yaml["shift_direction"]
        speed_factor = data_yaml["speed_factor"]

    def aug_all(self, data):
        shape = data.shape
        data_l = []
        data_r = []
        data_mono = []
        if shape[0] == 2:
            data_l, data_r = data[0, :], data[1, :]
            if self.do_aug_loud:
                aug_loud_out_l = self.aug_loud(data_l)
                aug_loud_out_r = self.aug_loud(data_r)
                self.aug_loud_out = np.vstack([aug_loud_out_l, aug_loud_out_r])
            if self.do_aug_noise:
                aug_noise_out_l = self.aug_noise(data_l)
                aug_noise_out_r = self.aug_noise(data_r)
                self.aug_noise_out = np.vstack([aug_noise_out_l, aug_noise_out_r])
            if self.do_aug_shift:
                aug_shift_out_l = self.aug_shift(data_l)
                aug_shift_out_r = self.aug_shift(data_r)
                self.aug_shift_out = np.vstack([aug_shift_out_l, aug_shift_out_r])
            if self.do_aug_speed:
                aug_speed_out_l = self.aug_speed(data_l)
                aug_speed_out_r = self.aug_speed(data_r)
                self.aug_speed_out = np.vstack([aug_speed_out_l, aug_speed_out_r])
        else:
            data_mono = data[0, :]
            if self.do_aug_loud:
                aug_loud_out_mono = self.aug_loud(data_mono)
                self.aug_loud_out = np.vstack([aug_loud_out_mono])
            if self.do_aug_noise:
                aug_noise_out_mono = self.aug_noise(data_mono)
                self.aug_noise_out = np.vstack([aug_noise_out_mono])
            if self.do_aug_shift:
                aug_shift_out_mono = self.aug_shift(data_mono)
                self.aug_shift_out = np.vstack([aug_shift_out_mono])
            if self.do_aug_speed:
                aug_speed_out_mono = self.aug_speed(data_mono)
                self.aug_speed_out = np.vstack([aug_speed_out_mono])

    def aug_loud(self, data):
        aug_loud_out = data * self.loudness_level
        return aug_loud_out

    def aug_noise(self, data):
        aug_noise_out = data + self.noise_factor * np.random.normal(0, 1, len(data))
        return aug_noise_out

    def aug_shift(self, data):
        shift = np.random.randint(self.sample_rate * self.shift_max)
        if self.shift_direction == 'right':
            shift = -shift
        elif self.shift_direction == 'both':
            direction = np.random.randint(0, 2)
            if direction == 1:
                shift = -shift
        aug_shift_out = np.roll(data, shift)
        if shift > 0:
            aug_shift_out[:shift] = 0
        else:
            aug_shift_out[shift:] = 0
        return aug_shift_out

    def aug_speed(self, data):
        N = len(data)
        yf = fft(data)
        aug_speed_out = irfft(yf, n=int(N * self.speed_factor))
        return aug_speed_out