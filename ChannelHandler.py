import numpy as np
from functools import reduce


class ChannelHandler:

    def __init__(self, channel_height, channel_width, range_of_brightness=256):
        self.channel_height = channel_height
        self.channel_width = channel_width
        self.range_of_brightness = range_of_brightness

    def get_histogram(self, channel):
        histogram = np.zeros(self.range_of_brightness)

        for brightness in channel:
            histogram[brightness] += 1

        return histogram

    def __bit_by_bit_processing(self, channel, logic_of_processing):
        processed_channel = list()

        for brightness in channel:
            processed_channel.append(logic_of_processing(brightness))

        return processed_channel

    def low_brightness(self, channel, max_out_brightness):

        def process_brightness(brightness):
            new_brightness = brightness - (self.range_of_brightness - 1 - max_out_brightness)
            return new_brightness if new_brightness > 0 else 0

        lowed_brightness = self.__bit_by_bit_processing(channel, process_brightness)

        return lowed_brightness

    def get_negative(self, channel):

        def process_negative(brightness):
            return self.range_of_brightness - 1 - brightness

        negative = self.__bit_by_bit_processing(channel, process_negative)

        return negative

    def __filter(self, channel, processing_neighborhood, size):
        indent = int(np.sqrt(size)) >> 1
        filtered = np.zeros(self.channel_width * self.channel_height)

        for row in range(indent, self.channel_height - indent):
            for col in range(indent, self.channel_width - indent):
                neighborhood = list()
                for neigh_row in range(row - indent, row + indent + 1):
                    for neigh_col in range(col - indent, col + indent + 1):
                        neighborhood.append(channel[neigh_row * self.channel_width + neigh_col])
                filtered[row * self.channel_width + col] = processing_neighborhood(neighborhood)

        return filtered

    def filter_by_harmonic_mean(self, channel, size=9):

        # G(f) = n / sum(1 / f(i)), i=1..n
        def logic_of_filtering_by_by_harmonic_mean(neighborhood):
            if 0 in neighborhood:
                harmonic = 0
            else:
                harmonic = len(neighborhood) / reduce(lambda h, f: h + (1 / f), neighborhood)
            return harmonic

        return self.__filter(channel, logic_of_filtering_by_by_harmonic_mean, size)

    def filter_by_median(self, channel, size=9):

        def logic_of_filtering_by_median(neighborhood):
            neighborhood = np.sort(neighborhood)
            return neighborhood[len(neighborhood) >> 1]

        return self.__filter(channel, logic_of_filtering_by_median, size)



