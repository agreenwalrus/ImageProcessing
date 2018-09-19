import math


class Object:

    def __init__(self):
        self.border = []
        self.pixels = []
        self.compactness = 0

    def add_border_pixel(self, pixel):
        self.border.append(pixel)

    def add_pixel(self, pixel):
        self.pixels.append(pixel)

    def get_pixels(self):
        return self.border + self.pixels

    def calculate_perimeter(self):
        return len(self.border)

    def calculate_area(self):
        return len(self.border) + len(self.pixels)

    def calculate_compactness(self):
        return (len(self.border) ** 2) / (len(self.border) + len(self.pixels))

    def calculate_elongation(self):
        x_sum = 0
        y_sum = 0
        for p in self.border + self.pixels:
            x_sum = x_sum + p[0]
            y_sum = y_sum + p[1]

        center_of_mass = (x_sum / (len(self.border) + len(self.pixels)), y_sum /
                          (len(self.border) + len(self.pixels)))

        m20 = Object.static_area_moment(self.border + self.pixels, center_of_mass, 2, 0)
        m02 = Object.static_area_moment(self.border + self.pixels, center_of_mass, 0, 2)
        m11 = Object.static_area_moment(self.border + self.pixels, center_of_mass, 1, 1)

        elongation = (m20 + m02 + math.sqrt((m20 - m02) ** 2 + 4*(m11 ** 2))) /\
                     (m20 + m02 - math.sqrt((m20 - m02) ** 2 + 4*(m11 ** 2)))

        return elongation

    def get_vector(self):
        return self.calculate_perimeter(), self.calculate_area(), self.calculate_compactness(), self.calculate_elongation()

    @staticmethod
    def static_area_moment(pixels, center_of_mass, i, j):
        m = 0
        for pixel in pixels:
           m += ((pixel[0] - center_of_mass[0]) ** i) * ((pixel[1] - center_of_mass[1]) ** j)
        return  m
