import sys

from Im.Clusterizer import Clusterizer
from Im.KMeans import KMeans
from Im.ObjectFinder import ObjectFinder
from Im.ImageHelper import ImageHelper
from Im.otsu import Otsu


names = ["P0001471.jpg"] # ["P0001460.jpg", "P0001461.jpg", "P0001468.jpg" ,"P0001469.jpg" ,"P0001471.jpg"]
names1 = ["P0001464.jpg", "P0001465.jpg", "P0001467.jpg" ,"P0001470.JPG" ,"P0001472.jpg"]
for image_name in names:

    sys.setrecursionlimit(1048576)

    image = ImageHelper.open_image("./source/lab2/easy/" + image_name)
    #filtered = ImageHelper.get_image_filtered_by_harmonic_mean(image, 49)
    greyscale = ImageHelper.get_greyscale_image(image)#filtered)

    div = Otsu.devide_classes(greyscale)
    print("division: ", div)
    bin_im = ImageHelper.get_binorized_image(greyscale, div)


    #filtered = ImageHelper.get_image_filtered_by_median(bin_im, 49)

    erosion = ImageHelper.get_image_with_erosion(bin_im, 4)
    building = ImageHelper.get_image_with_building(erosion, 4)

    objects = ObjectFinder.find_object(building)

    vectors = []
    for i in range(len(objects)):
        vectors.append((i, objects[i].get_vector()))

    #normalization
    normalize_vectors = []
    for v in vectors:
        normalize_vectors.append((v[0], []))
    for i in range(len(vectors[0][1])):
        array = []
        for v in vectors:
            array.append(v[1][i])

        min_value = min(array)
        max_value = max(array)

        for j in range(len(vectors)):
            normalize_vectors[j][1].append((vectors[j][1][i] - min_value) / (max_value - min_value))

    clusters = KMeans.k_means(normalize_vectors, 7, KMeans.evclid_distance)
    clust_image = Clusterizer.get_clustered_image(image, objects, clusters)
    #ImageHelper.show_histogram(image, "source " + image_name)
    #ImageHelper.show_histogram(bin_im, "bin " + image_name)
    #ImageHelper.save_image(bin_im, "./source/lab2/result/" + "bin.jpg")
    #ImageHelper.save_image(erosion, "./source/lab2/result/" + "erosion.jpg")
    ImageHelper.save_image(clust_image, "./source/lab2/result/" + image_name)