from Im.ImageHelper import ImageHelper


def lab():
    IMAGE_NAME = "lena"
    STUDENT_IMAGE_NAME = "beautiful"
    MAX_BRIGHTNESS = 225
    FILTER_SIZE = 9
    PERCENT_OF_NOISE = 3

    image = ImageHelper.open_image("./source/lab1/" + IMAGE_NAME + ".jpg")
    f = ImageHelper.show_histogram(image, "Source " + IMAGE_NAME)

    grey = ImageHelper.get_greyscale_image(image)
    ImageHelper.save_image(grey, "./source/lab1/result/Greyscale_" + IMAGE_NAME)
    ImageHelper.show_histogram(grey, "Greyscale " + IMAGE_NAME)

    noise_mc = ImageHelper.get_image_with_some_noise(image, percent=PERCENT_OF_NOISE)
    ImageHelper.save_image(noise_mc, "./source/lab1/result/Noise_" + IMAGE_NAME)
    ImageHelper.show_histogram(noise_mc, "Noise " + IMAGE_NAME)

    filtered = ImageHelper.get_image_filtered_by_harmonic_mean(noise_mc, size=FILTER_SIZE)
    ImageHelper.save_image(filtered, "./source/lab1/result/HarmonicMean_" + IMAGE_NAME)
    ImageHelper.show_histogram(filtered, "HarmonicMean " + IMAGE_NAME)

    filtered = ImageHelper.get_image_filtered_by_median(noise_mc, size=FILTER_SIZE)
    ImageHelper.save_image(filtered, "./source/lab1/result/Median_" + IMAGE_NAME)
    ImageHelper.show_histogram(filtered, "Median " + IMAGE_NAME)

    image = ImageHelper.open_image("./source/lab1/" + STUDENT_IMAGE_NAME + ".jpg")
    ImageHelper.show_histogram(image, "Source " + STUDENT_IMAGE_NAME)

    lowed_brightness = ImageHelper.get_image_with_lowed_brightness(image, max_out_brightness=MAX_BRIGHTNESS)
    ImageHelper.save_image(lowed_brightness, "./source/lab1/result/LowedBrightness_" + STUDENT_IMAGE_NAME)
    ImageHelper.show_histogram(lowed_brightness, "LowedBrightness " + STUDENT_IMAGE_NAME)
