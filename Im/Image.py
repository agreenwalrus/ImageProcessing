class Image:

    def __init__(self, channels, height, width, range_of_brightness):
        self.__range_of_brightness = range_of_brightness
        self.__width = width
        self.__height = height
        self.__channels = channels

    def get_channels(self):
        return self.__channels

    def get_range_of_brightness(self):
        return self.__range_of_brightness

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
