import math
import numpy as np
from copy import copy
import random


class KMeans:
    @staticmethod
    def evclid_distance(a, b):
        distance = 0
        for i in range(len(a)):
            distance = distance + (b[i] - a[i]) ** 2
        return math.sqrt(distance)

    @staticmethod
    def sity_distance(a, b):
        distance = 0
        for i in range(len(a)):
            distance = distance + abs(b[i] - a[i])
        return math.sqrt(distance)

    @staticmethod
    def chees_distance(a, b):
        distance = []
        for i in range(len(a)):
            distance.append(abs(b[i] - a[i]))
        return max(distance)

    @staticmethod
    def get_center_of_mass(points, center_of_mass):
        if len(points) == 0:
            return center_of_mass
        np_array = []

        for p in points:
            np_array.append(np.array(p[1]))

        vec = sum(np_array) / len(points)

        return (-1, list(vec))

    @staticmethod
    def k_means(vectors, k, distance_method):
        def fan(points, center_of_mass):
            # расчитать кластеры
            clusters = [[]] * len(center_of_mass)
            for i in range(len(center_of_mass)):
                clusters[i] = []

            for p in points:
                dist = list(map(lambda x: distance_method(x[1], p[1]), center_of_mass))
                c_n = dist.index(min(dist))
                clusters[c_n].append(p)

            # расчитать новые центры масс
            new_center_of_mass = []
            i = 0
            for c in clusters:
                new_center_of_mass.append(KMeans.get_center_of_mass(c, center_of_mass[i]))
                i+=1

            # cравнить цм
            if center_of_mass == new_center_of_mass:
                return clusters
            else:
                return fan(points, new_center_of_mass)

        c_o_m = random.sample(vectors, k)
        return fan(vectors, c_o_m)