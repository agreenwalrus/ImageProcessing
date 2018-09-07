import numpy as np
import random
import copy


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

    @staticmethod
    def __byte_checker(byte):
        return 0 if byte <= 0 else 255 if byte >= 255 else byte

    def __bit_by_bit_processing(self, channel, logic_of_processing):
        processed_channel = list()

        for brightness in channel:
            processed_channel.append(ChannelHandler.__byte_checker(logic_of_processing(brightness)))

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

#bad algorithm
    def get_log_correction(self, channel, constant):

        def process_logarithmic_correction(brightness, c=constant):
            return int(c * int(np.log2(1 + brightness)))

        logarithmic_corrected = self.__bit_by_bit_processing(channel, process_logarithmic_correction)
        return logarithmic_corrected


    def __filter(self, channel, processing_neighborhood, size):
        indent = int(np.sqrt(size)) >> 1
        filtered = np.zeros(self.channel_width * self.channel_height)

        for row in range(indent, self.channel_height - indent):
            for col in range(indent, self.channel_width - indent):
                neighborhood = list()
                for neigh_row in range(row - indent, row + indent + 1):
                    for neigh_col in range(col - indent, col + indent + 1):
                        neighborhood.append(channel[neigh_row * self.channel_width + neigh_col])
                filtered[row * self.channel_width + col] = \
                    ChannelHandler.__byte_checker(processing_neighborhood(neighborhood))

        return list(map(lambda x: int(x), filtered))

    def filter_by_harmonic_mean(self, channel, size=9):

        # G(f) = n / sum(1 / f(i)), i=1..n
        def logic_of_filtering_by_by_harmonic_mean(neighborhood):
            if 0 in neighborhood:
                harmonic = 0
            else:
                s = 0
                for n in neighborhood:
                    s += 1 / n
                harmonic = len(neighborhood) / s
            return int(harmonic)

        return self.__filter(channel, logic_of_filtering_by_by_harmonic_mean, size)

    def filter_by_median(self, channel, size=9):

        def logic_of_filtering_by_median(neighborhood):
            neighborhood = np.sort(neighborhood)
            return neighborhood[len(neighborhood) >> 1]

        return self.__filter(channel, logic_of_filtering_by_median, size)





