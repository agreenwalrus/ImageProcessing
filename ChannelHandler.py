import numpy as np

class ChannelHandler:

    def __init__(self, range_of_brigntness=256):
        self.range_of_brightness = range_of_brigntness

    def get_histogram(self, channel):
        histogram = np.zeros(self.range_of_brightness)
        for brightness in channel:
            histogram[brightness] += 1

        return histogram

    def get_negative(self, channel):
        negative = list()
        for brightness in channel:
            negative.append(self.range_of_brightness - brightness)

        return negative

    def get_handled_by_harmonic_mean_filter(self, channel):
        pass

    def get_handled_by_median_filter(self, channel, size=9):
        pass

    def change_brightness(self, channel):
        pass


