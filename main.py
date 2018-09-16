


from Im.ImageHelper import ImageHelper
from Im.otsu import Otsu


names = ["P0001460.jpg", "P0001461.jpg", "P0001468.jpg" ,"P0001469.jpg" ,"P0001471.jpg"]
names1 = ["P0001464.jpg", "P0001465.jpg", "P0001467.jpg" ,"P0001470.JPG" ,"P0001472.jpg"]
for image_name in names:

    image = ImageHelper.open_image("./source/lab2/easy/" + image_name)
    filtered = ImageHelper.get_image_filtered_by_harmonic_mean(image, 49)
    greyscale = ImageHelper.get_greyscale_image(filtered)

    div = Otsu.devide_classes(greyscale)
    print("division: ", div)
    bin_im = ImageHelper.get_binorized_image(greyscale, div)

    ##filtered = ImageHelper.get_image_filtered_by_median(bin_im, 49)

    ImageHelper.show_histogram(image, "source " + image_name)
    ImageHelper.show_histogram(bin_im, "bin " + image_name)
    ImageHelper.save_image(ImageHelper.get_image_filtered_by_median(bin_im, 49), "./source/lab2/result/" + image_name)


