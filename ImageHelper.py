import matplotlib.pyplot as plt
import PIL
from Image import Image
from ChannelHandler import ChannelHandler
import copy
import random

class ImageHelper:

    G = 0
    R = 0
    G = 1
    B = 2
    RGB_MODE = 'RGB'
    GREYSCALE_MODE = 'L'
    RGB = 3
    RANGE_OF_BRIGHTNESS = 256

    @staticmethod
    def open_image(path):
        image = PIL.Image.open(path)
        pixels = list(image.getdata())
        channels = ImageHelper.__channel_converter(pixels, image.mode)

        return Image(channels, image.height, image.width, ImageHelper.RANGE_OF_BRIGHTNESS)

    # converts [[just r], [just g], [just b]] to [(r, g, b, a), ...]
    # mode could be P-pallete or RGB
    @staticmethod
    def __pixel_converter(image):
        pix = []

        if len(image.get_channels()) == ImageHelper.RGB:
            for i in range(image.get_width() * image.get_height()):
                pix.append((image.get_channels()[0][i],
                            image.get_channels()[1][i],
                            image.get_channels()[2][i],
                            255))
        else:
            pix = copy.copy(image.get_channels()[0])

        return pix

    #converts [(r, g, b, a), ...] to [[just r], [just g], [just b]]
    @staticmethod
    def __channel_converter(pix, mode):

        if mode == "RGB":
            channels = [list(), list(), list()]
            for i in range(ImageHelper.RGB):
                for j in range(len(pix)):
                    channels[i].append(pix[j][i])
        else:
            channels = [copy.copy(pix)]

        return channels

    @staticmethod
    def __get_channel_handler(image):
        return ChannelHandler(image.get_height(),
                            image.get_width(),
                            image.get_range_of_brightness())


    @staticmethod
    def show_histogram(image, title):

        if len(image.get_channels()) == 1:
            colors = ['k']
        else:
            colors = ['r', 'g', 'b']

        channel_handler = ChannelHandler(image.get_height(),
                                         image.get_width(),
                                         image.get_range_of_brightness())

        color_ind = 0
        for channel in image.get_channels():
            histogram = channel_handler.get_histogram(channel)
            plt.title(title)
            plt.xlabel("Brightness")
            plt.ylabel("Frequency")
            plt.plot(range(image.get_range_of_brightness()), histogram, color=colors[color_ind])
            plt.show()
            color_ind += 1

    @staticmethod
    def save_image(image, file_name):
        mode = ImageHelper.GREYSCALE_MODE if len(image.get_channels()) == 1 else ImageHelper.RGB_MODE
        im = PIL.Image.new(mode, (image.get_width(), image.get_height()))
        pix = ImageHelper.__pixel_converter(image)
        im.putdata(pix)
        im.save(file_name + ".jpg", 'JPEG')

    @staticmethod
    def get_negative_image(image):
        new_channels = list()
        channel_handler = ImageHelper.__get_channel_handler(image)

        for channel in image.get_channels():
            new_channels.append(channel_handler.get_negative(channel))

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())

    @staticmethod
    def get_image_with_lowed_brightness(image, max_out_brightness):
        new_channels = list()
        channel_handler = ImageHelper.__get_channel_handler(image)

        for channel in image.get_channels():
            new_channels.append(channel_handler.low_brightness(channel, max_out_brightness))

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())

    @staticmethod
    def get_image_with_logarithmic_correction(image, constant=1):
        new_channels = list()
        channel_handler = ImageHelper.__get_channel_handler(image)

        for channel in image.get_channels():
            new_channels.append(channel_handler.get_log_correction(channel, constant))

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())

    @staticmethod
    def get_image_with_some_noise(image, percent=10):

        indexes = random.sample(range(len(image.get_channels()[0])),
                                int(len(image.get_channels()[0]) * (percent / 100)))
        new_channels = list()
        for channel in image.get_channels():
            new_channels.append(copy.copy(channel))

        for ind in indexes:
            for channel in new_channels:
                channel[ind] = 0

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())

    #ITU-R 601-2 luma transform
    @staticmethod
    def get_greyscale_image(image):
        if len(image.get_channels()) == ImageHelper.RGB:
            result = []
            for ind in range(len(image.get_channels()[ImageHelper.R])):
                grey_byte = \
                    int(image.get_channels()[ImageHelper.R][ind] * 299 / 1000 + \
                        image.get_channels()[ImageHelper.G][ind] * 587 / 1000 + \
                        image.get_channels()[ImageHelper.B][ind] * 114 / 1000)
                result.append(grey_byte)
        else:
            result = copy.copy(image.get_channels()[ImageHelper.G])

        return Image([result],
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())



    @staticmethod
    def get_image_filtered_by_median(image, size=9):
        new_channels = list()
        channel_handler = ImageHelper.__get_channel_handler(image)

        for channel in image.get_channels():
            new_channels.append(channel_handler.filter_by_median(channel, size))

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())

    @staticmethod
    def get_image_filtered_by_harmonic_mean(image, size=9):
        new_channels = list()
        channel_handler = ImageHelper.__get_channel_handler(image)

        for channel in image.get_channels():
            new_channels.append(channel_handler.filter_by_harmonic_mean(channel, size))

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())


