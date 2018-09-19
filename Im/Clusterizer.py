class Clusterizer:
    @staticmethod
    def get_clustered_image(image, objects, clusters):
        colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (0,0,0)]
        color_number = 0
        for cluster in clusters:
            for o in cluster:
                for p in objects[o[0]].get_pixels():
                    image.get_channels()[0][p[0] * image.get_width() + p[1]] = colors[color_number][0]
                    image.get_channels()[1][p[0] * image.get_width() + p[1]] = colors[color_number][1]
                    image.get_channels()[2][p[0] * image.get_width() + p[1]] = colors[color_number][2]

            color_number += 1

        return image

