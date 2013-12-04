import sys
from numpy import zeros
from cv2 import imread, imwrite

def load_images(path_source_1, path_source_2):


        #the images are loaded, and stored as OpenCV mat objects
        image_source_1 = imread(path_source_1)
        image_source_2 = imread(path_source_2)

        return image_source_1, image_source_2

def find_diff(image_source_1, image_source_2):
    if len(image_source_1) != len(image_source_2):
        print('image dimensions do not match')

    diff_array = zeros(image_source_2.shape)

    for i in range(image_source_1.shape[0]):
        for r in range(image_source_1.shape[1]):
            if image_source_1[i, r].all() != image_source_2[i, r].all():
                diff_array[i, r] = image_source_1[i, r]


    return diff_array




if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) < 2:
        print('not enough parameters')
        sys.exit(0)
    elif len(args)==3:
        path_source_1, path_source_2, path_dest = args
    elif len(args)==2:
        path_source_1, path_source_2 = args
        path_dest = 'diff.'+path_source_1.split('.')[1]

    raw_input()


    image_source_1, image_source_2 = load_images('core.jpg', 'core2.jpg')
    diff = find_diff(image_source_1, image_source_2)

    imwrite(path_dest, diff)