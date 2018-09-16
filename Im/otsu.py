from Im.Image import *
from Im.ImageHelper import *
import math


class Otsu:

    @staticmethod
    def culculate_intensity_sum(histogram):
        sum = 0
        for intensity in range(len(histogram)):
            sum += intensity * histogram[intensity]
        return sum


    @staticmethod
    def devide_classes(image):
        greyscale_image = ImageHelper.get_greyscale_image(image)
        histogram = ImageHelper.get_histograms(greyscale_image)[0]

        amount_of_all_pixels = image.get_height() * image.get_width()
        all_intensity_sum = Otsu.culculate_intensity_sum(histogram)

        best_dispersion = 0
        best_division = 0

        first_class_amount_of_pixels = 0
        first_class_itensity = 0

        for current_division in range(len(histogram) - 1):

            first_class_amount_of_pixels += histogram[current_division]
            first_class_itensity += current_division * histogram[current_division]

            first_class_probability = first_class_amount_of_pixels / amount_of_all_pixels
            second_class_probability = 1 - first_class_probability

            first_class_mean = first_class_itensity / first_class_amount_of_pixels
            second_class_mean = (all_intensity_sum - first_class_itensity) / \
                                (amount_of_all_pixels - first_class_amount_of_pixels)

            delta = (first_class_mean - second_class_mean)
            current_dispersion = (delta ** 2) * first_class_probability * second_class_probability

            if current_dispersion > best_dispersion:
                best_dispersion = current_dispersion
                best_division = current_division

        return best_division


