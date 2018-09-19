import copy
from Im.Image import Image
from Im.Object import Object


class ObjectFinder:

    @staticmethod
    def find_object(image):
        def rec(x, y, name, chanel, w, h, flags, object):
            if x < 0 or x > (h - 1):
                return
            if y < 0 or y > (w - 1):
                return

            if chanel[x * w + y] == 255:
                if flags_matrix[x][y] == 0:
                    flags[x][y] = name
                    chanel[x * w + y] = 255 if name % 2 == 0 else 120

                    border_pixel = False
                    if x != 0 and chanel[(x - 1) * w + y] == 0:
                        border_pixel = True
                    if x != h - 1 and chanel[(x + 1) * w + y] == 0:
                        border_pixel = True
                    if y != 0 and chanel[x * w + y - 1] == 0:
                        border_pixel = True
                    if y != w - 1 and chanel[x * w + y + 1] == 0:
                        border_pixel = True

                    if border_pixel:
                        object.add_border_pixel((x,y))
                    else:
                        object.add_pixel((x,y))

                    rec(x - 1, y, name, chanel, w, h, flags, object)
                    rec(x + 1, y, name, chanel, w, h, flags, object)
                    rec(x, y - 1, name, chanel, w, h, flags, object)
                    rec(x, y + 1, name, chanel, w, h, flags, object)

                    return object

        flags_matrix = [[0] * image.get_width() for _ in range(image.get_height())]
        chanel = copy.copy(image.get_channels()[0])

        current_object_name = 1
        objects = []
        for row in range(image.get_height()):
            for column in range(image.get_width()):
                if flags_matrix[row][column] == 0:
                    if chanel[row * image.get_width() + column] == 255:

                        objects.append(rec(row, column, current_object_name,
                            chanel, image.get_width(), image.get_height(),
                            flags_matrix, Object()))

                        current_object_name += 1

        return objects
        # return Image([chanel],
        #              image.get_height(),
        #              image.get_width(),
        #              image.get_range_of_brightness())