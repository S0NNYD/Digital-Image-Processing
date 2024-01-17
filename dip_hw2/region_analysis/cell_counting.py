import cv2
from dip import *

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes a input:
        image: binary image
        return: a list/dict of regions"""

        regions = dict()
        R = zeros(image.shape, dtype=int)
        count = 0

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] == 0:
                    top = R[i - 1][j]
                    left = R[i][j - 1]
                    if top == 0 and left == 0:
                        count += 1
                        R[i][j] = count
                        regions[R[i][j]] = []
                        regions[R[i][j]].append((i, j))
                    elif (top == 0 and left != 0) or (top != 0 and left != 0 and top == left):
                        R[i][j] = left
                        regions[left].append((i, j))
                    elif top != 0 and left == 0:
                        R[i][j] = top
                        regions[top].append((i, j))
                    else:
                        R[i][j] = top
                        R[i][j - 1] = top

                        regions[top].append((i, j))
                        regions[top].extend(regions[left])
                        regions[left].clear()

        return regions


    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list/dict of pixels in a region
        returns: region statistics"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        # ignore cells smaller than 15px
        for key, val in list(region.items()):
            if len(val) < 15:
                region.pop(key)

        stats = region
        count = 0  # region number

        for key, value in list(region.items()):
            count += 1
            area = len(value)

            # calculate centroid
            sum_x, sum_y = 0, 0
            for i in range(area):
                sum_x += value[i][0]
                sum_y += value[i][1]

            center_x = int(sum_x / area)
            center_y = int(sum_y / area)
            centroid = (center_x, center_y)

            stats[key] = []
            stats[key].append(centroid)
            stats[key].append(area)
            print("Region: ", count, "Area: ", area, "Centroid", centroid)

        return stats

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text.
        takes as input
        image: a list/dict of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        # flip the image color to get a black background and white objects
        completed_image = 255 - image.copy()

        for key, val in list(stats.items()):
            centroid = val[0]
            area = val[1]
            putText(completed_image, '*' + str(key) + ',' + str(area), (centroid[1], centroid[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
        return completed_image

