class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        # compute the histogram
        for i in range(0, image.shape[0]):
            for j in range(0, image.shape[1]):
                hist[image[i,j]] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram it to find the otsu's threshold assuming that the input hstogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold)"""

        threshold = 0
        # compute probabilities
        total = sum(hist)
        prob = [0]*256
        for i in range(0, 256):
            prob[i] = hist[i]/total

        list_of_weights = []
        # iterate through all possible thresholds (t=0 to t=255)
        for t in range(0, 256):
            # compute weights (q1, q2)
            q1 = sum(prob[0:t])
            q2 = sum(prob[t:256])

            # compute means (u1,u2) and intra-class variance (sigma1, sigma2)
            if q1 == 0:
                u1 = 0
                sigma1 = 0
            else:
                u1 = sum([i*prob[i] for i in range(0, t)]) / q1
                sigma1 = sum([(i-u1)**2 * prob[i] for i in range(0, t)]) / q1
            if q2 == 0:
                u2 = 0
                sigma2 = 0
            else:
                u2 = sum([i*prob[i] for i in range(t, 256)]) / q2
                sigma2 = sum([(i-u2)**2 * prob[i] for i in range(t, 256)]) / q2

            #compute weighted sum of intra class variance
            sigma_w = q1*sigma1 + q2*sigma2
            list_of_weights.append(sigma_w)

        # find the threshold that minimizes the weighted sum of intra class variance
        threshold = list_of_weights.index(min(list_of_weights))
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        histogram = BinaryImage.compute_histogram(self, bin_img)
        threshold = BinaryImage.find_otsu_threshold(self, histogram)

        for i in range(0, bin_img.shape[0]):
            for j in range(0, bin_img.shape[1]):
                if bin_img[i, j] <= threshold:
                    bin_img[i, j] = 0
                else:
                    bin_img[i, j] = 255

        return bin_img


