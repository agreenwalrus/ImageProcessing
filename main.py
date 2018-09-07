from ImageHelper import ImageHelper
import matplotlib.pyplot as plt
import numpy as np

IMAGE_NAME = "students_RGB"
MAX_BRIGHTNESS = 225
FILTER_SIZE = 9
CONSTANT_FOR_LOG_CORR = 30

image = ImageHelper.open_image("./source/" + IMAGE_NAME + ".jpg")
ImageHelper.show_histogram(image, "Source")

grey = ImageHelper.get_greyscale_image(image)
ImageHelper.save_image(grey, "./source/result/Greyscale_" + IMAGE_NAME + ".jpg")

lowed_brightness = ImageHelper.get_image_with_lowed_brightness(grey, MAX_BRIGHTNESS)
ImageHelper.save_image(lowed_brightness, "./source/result/LowedBrightness_" + IMAGE_NAME)
ImageHelper.show_histogram(lowed_brightness, "LowedBrightness " + IMAGE_NAME)

"""
noised = ImageHelper.get_image_with_some_noise(image, 5)
ImageHelper.save_image(noised, "./source/result/Noise_" + IMAGE_NAME)
ImageHelper.show_histogram(noised, "Noise " + IMAGE_NAME)

filtered_by_median = ImageHelper.get_image_filtered_by_median(noised, FILTER_SIZE)
ImageHelper.save_image(filtered_by_median, "./source/result/ByMedian_" + IMAGE_NAME)
ImageHelper.show_histogram(filtered_by_median, "ByMedian " + IMAGE_NAME)

lowed_brightness = ImageHelper.get_image_with_lowed_brightness(image, MAX_BRIGHTNESS)
ImageHelper.save_image(lowed_brightness, "./source/result/LowedBrightness_" + IMAGE_NAME)
ImageHelper.show_histogram(lowed_brightness, "LowedBrightness " + IMAGE_NAME)

negative = ImageHelper.get_negative_image(image)
ImageHelper.save_image(negative, "./source/result/Negative_" + IMAGE_NAME)
ImageHelper.show_histogram(negative, "Negative " + IMAGE_NAME)

filtered_by_median = ImageHelper.get_image_filtered_by_median(image, FILTER_SIZE)
ImageHelper.save_image(filtered_by_median, "./source/result/ByMedian_" + IMAGE_NAME)
ImageHelper.show_histogram(filtered_by_median, "ByMedian " + IMAGE_NAME)

filtered_by_harmonic_mean = ImageHelper.get_image_filtered_by_harmonic_mean(image, FILTER_SIZE)
ImageHelper.save_image(filtered_by_harmonic_mean, "./source/result/ByHarmonicMean_" + IMAGE_NAME)
ImageHelper.show_histogram(filtered_by_harmonic_mean, "ByHarmonicMean " + IMAGE_NAME)
"""



