import matplotlib.pyplot as plt
from PIL import Image
from ChannelHandler import ChannelHandler


class ImageHelper:

    def __init__(self, path):

        self.__image = Image.open(path)
        self.__pixels = list(self.__image.getdata())
        self.__range_of_brightness = 256 if not self.__image.getcolors() else self.__image.getcolors()
        self.__channel_handler = ChannelHandler(self.__image.size[0],
                                                self.__image.size[1],
                                                self.__range_of_brightness)
        self.__channels = self.__channel_converter(self.__pixels)

    # converts [[just r], [just g], [just b]] to [(r, g, b, a), ...]
    def __pixel_converter(self):
        pix = []

        for i in range(self.__image.size[0] * self.__image.size[1]):
            pix.append((self.__channels[0][i], self.__channels[1][i], self.__channels[2][i]))

        return pix

    #converts [(r, g, b, a), ...] to [[just r], [just g], [just b]]
    def __channel_converter(self, pix):
        channels = [list(), list(), list()]

        for i in range(3):
            for j in range(len(pix)):
                channels[i].append(pix[j][i])

        return channels

    def show_histogram(self, title):

        if len(self.__channels) == 1:
            colors = ['k']
        else:
            colors = ['r', 'g', 'b']

        color_ind = 0
        for channel in self.__channels:
            histogram = self.__channel_handler.get_histogram(channel)
            plt.title(title)
            plt.xlabel("Brightness")
            plt.ylabel("Frequency")
            plt.plot(range(self.__range_of_brightness), histogram, color=colors[color_ind])
            plt.show()
            color_ind += 1

    def save_image(self, file_name):
        mode = 'P' if len(self.__channels) == 1 else 'RGB'
        image = Image.new(mode, (self.__image.size[0], self.__image.size[1]))
        pix = self.__pixel_converter()
        image.putdata(pix)
        image.save("./source/" + file_name + ".jpg", 'JPEG')


