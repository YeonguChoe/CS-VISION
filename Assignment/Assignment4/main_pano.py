import hw_utils as utils
import sys
import numpy as np
import matplotlib.pyplot as plt
import os.path as op
sys.path = ['../lib'] + sys.path
path = './data/'


def create_pano(
        image_list, ratio_thres,
        canvas_height, canvas_width,
        num_iter, tol, figsize=(20, 20)):
    """
    This function creates a panorama using a list of images.
    Inputs:
        image_list: a list of str, the path to each image (without file extensions).
        ratio_thres: the ratio test threshold in `FindBestMatches`
        canvas_height, canvas_width: The dimension of the canvas
        num_iter: num of iterations of performing RANSAC to find the homography matrix.
        tol: tolerance for keypoint projection
    """
    # Get the matches from `FindBestMatches`
    # xy_src_list: np.array, (matches, 2) in xy format
    # xy_ref_list: np.array, (matches, 2) in xy format
    # im_list: a list of images in np.array
    xy_src_list, xy_ref_list, im_list = utils.PrepareData(
        image_list, ratio_thres)

    # Use the matches to estimate a homography matrix to the ref image frame
    # for each source image. Then project each source image to the reference
    # frame using the homography matrix.
    wrap_list = utils.ProjectImages(
        xy_src_list, xy_ref_list, im_list,
        canvas_height, canvas_width, num_iter, tol)

    # Merge the projected images above
    # Note: the first element is the reference image in warp_list
    result = utils.MergeWarppedImages(
        canvas_height, canvas_width, wrap_list)

    # show the final panorama
    plt.figure(figsize=figsize)
    plt.imshow(result)
    plt.show()
    # save image
    # plt.imsave('Q2-4.jpg', result)


def main():
    canvas_height = 600
    canvas_width = 1000
    image_list = ['Rainier1', 'Rainier2', 'Rainier3',
                  'Rainier4', 'Rainier5', 'Rainier6']

    # fountain40.png, garden034.png, and irving_out365.png

    # # fountain40
    # canvas_height = 1300
    # canvas_width = 2300
    # image_list = ['fountain4', 'fountain0']

    # # garden034
    # canvas_height = 1180
    # canvas_width = 2300
    # image_list = ['garden0', 'garden3', 'garden4']

    # # irving_out365
    # canvas_height = 1600
    # canvas_width = 2900
    # image_list = ['irving_out3', 'irving_out6', 'irving_out5']

    tol = 100
    num_iter = 30
    ratio_thres = 0.5
    image_list = [op.join(path, im) for im in image_list]
    create_pano(image_list, ratio_thres, canvas_height, canvas_width,
                num_iter, tol, figsize=(20, 20))


if __name__ == '__main__':
    main()
