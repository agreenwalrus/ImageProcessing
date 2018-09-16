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
        return -byte if byte <= 0 else 255 if byte >= 255 else byte

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

    def make_some_noise(self, channel, percent=10):
        NOISE = 255

        indexes = random.sample(range(len(channel)),
                                int(len(channel) * (percent / 100)))

        new_channel = copy.copy(channel)
        for ind in indexes:
            new_channel[ind] = NOISE

        return new_channel


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

    def binorize_channel(self, channel, division):
        return list(map(lambda x: 0 if x < division else 255, channel))

    def binorize_adaptive_channel(self, channel, block_size, addition_percent=15):

        def get_integral_channel(channel):
            integral_channel = [[0] * self.channel_width for _ in range(self.channel_height)]

            for column in range(self.channel_width):
                sum = 0
                for row in range(self.channel_height):
                    sum += channel[row * self.channel_width + column]
                    if column == 0:
                        integral_channel[row][column] = sum
                    else:
                        integral_channel[row][column] = integral_channel[row][column - 1] + sum

            return integral_channel

        integral_image = get_integral_channel(channel)
        result_channel = [0] * self.channel_width * self.channel_height

        for column in range(self.channel_width):
            for row in range(self.channel_height):
                x1 = column - (block_size / 2)
                x2 = column + (block_size / 2)
                y1 = row - (block_size / 2)
                y2 = row + (block_size / 2)

                x1 = 0 if x1 < 0 else int(x1)
                x2 = self.channel_width - 1 if x2 >= self.channel_width else int(x2)
                y1 = 0 if y1 < 0 else int(y1)
                y2 = self.channel_height - 1 if y2 >= self.channel_height else int(y2)

                amount_of_pixeles = (x2 - x1) * (y2 - y1)

                sum = integral_image[y2][x2] - integral_image[y1][x2] - integral_image[y2][x1] + integral_image[y1][x1]

                if channel[row * self.channel_width + column] * amount_of_pixeles <= sum * (100 - addition_percent) / 100:
                    result_channel[row * self.channel_width + column] = 0
                else:
                    result_channel[row * self.channel_width + column] = 255

        return result_channel






