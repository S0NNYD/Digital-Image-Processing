"""dip_hw0.py: Starter file to run homework 0"""

__author__ = "Khadija Khaldi"
# revised by Zhenggang Li
# revised by Shishir Shah
# revised by Pranav Mantini
__version__ = "1.0.1"

from dip import *
import sys
from image_op import operations


def display_image(window_name, image):
    """A function to display image"""
    namedWindow(window_name)
    imshow(window_name, image)
    waitKey(0)


def blend_compass(image):
    shape = image.shape
    image = array(image, uint8)
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    font = FONT_HERSHEY_SIMPLEX

    n_position = (40, shape[1]//2)
    s_position = (shape[0]-20, shape[1] // 2)

    w_position = (shape[0]//2, 20)
    e_position = (shape[0]//2, shape[1] - 40)

    putText(image, 'N', (n_position[1], n_position[0]), font,
                        fontScale, color, thickness, LINE_AA)

    putText(image, 'S', (s_position[1], s_position[0]), font,
                        fontScale, color, thickness, LINE_AA)

    putText(image, 'E', (e_position[1], e_position[0]), font,
                        fontScale, color, thickness, LINE_AA)

    putText(image, 'W', (w_position[1], w_position[0]), font,
                        fontScale, color, thickness, LINE_AA)

    return image


def main():
    """ The main function that parses input arguments, calls the appropriate
     method and writes the output image"""

    #Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-if", "--image-foreground", dest="image_f",
                        help="specify the name of the foreground image", metavar="IMAGEFORE", default="falcon.png")
    parser.add_argument("-ib", "--image-b", dest="image_b",
                        help="specify the name of the background image", metavar="IMAGEBACK", default="dstar.png")

    parser.add_argument("-fd", "--flip-d", dest="flip_d",
                        help="specify the direction to flip along (horizontal or vertical)", metavar="FLIPDIR", default="horizontal")

    parser.add_argument("-tc", "--target-color", dest="target_color", type=int, nargs='+',
                        help="specify the target color for chroma keying", metavar="TARGETCOLOR", default=[0, 200, 0])

    parser.add_argument('-t', '--threshold', dest='threshold',
                        help='specify the threshold for keying', metavar='THRESHOLD', default=150)

    args = parser.parse_args()

    # Load image
    if args.image_f is None:
        print("Please specify the name of foregraound image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image_foreground = imread(args.image_f)

    if args.image_b is None:
        print("Please specify the name of background image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image_background = imread(args.image_b)

    if args.flip_d not in ["horizontal", "vertical"]:
        print('Invalid direction %s, using horizontal' % args.flip_d)
        direction = "horizontal"
    else:
        direction = args.flip_d

    if args.target_color is None:
        print('Targeted Color not specified using default [0, 0, 255]')
        target_color = [0, 200, 0]
    else:
        target_color = [int(i) for i in args.target_color]
        if len(target_color) > 3:
            print("Intensity of each color channel should be between 0 and 255")
            print("Using default value (0, 0, 255)")
            target_color = [0, 200, 0]

        for i in target_color:
            if i < 0 or i > 255:
                print("Intensity of each color channel should be between 0 and 255")
                print("Using default value (0, 0, 255)")
                target_color = [0, 200, 0]

    if args.threshold is None:
        print('Threshold is not specified using default (180)')
        threshold = 150
    else:
        threshold = float(args.threshold)

    # Write output file
    outputDir = 'output/'
    operation_obj = operations.Operation()

    compass_image = blend_compass(input_image_background)

    flipped_image = operation_obj.flip(compass_image, direction)
    output_image_name = outputDir + 'flipped_' + direction + ".jpg"
    imwrite(output_image_name, flipped_image)

    chroma_keyed_image =operation_obj.chroma_keying(input_image_foreground, input_image_background, target_color=target_color, threshold=threshold)
    output_image_name = outputDir + 'chroma_keyed_' + "_".join([str(k) for k in target_color]) + ".jpg"
    imwrite(output_image_name, chroma_keyed_image)


if __name__ == "__main__":
    main()







