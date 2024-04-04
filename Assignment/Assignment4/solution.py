import numpy as np
import cv2
import math
import random


# descriptors1: list of normalized descriptor vector for 1st image
# descriptors2: list of normalized descriptor vector for 2nd image
def FindBestMatches(descriptors1: np.ndarray, descriptors2: np.ndarray, threshold: float) -> [[np.ndarray, np.ndarray]]:
    assert isinstance(descriptors1, np.ndarray)
    assert isinstance(descriptors2, np.ndarray)
    assert isinstance(threshold, float)
    # Step1: Initialize empty list
    matched_pairs = []

    # Step2: Iterate over the list of 1st descriptor vector
    for i in range(0, descriptors1.shape[0], 1):
        # Step 3: Initialize list of angle between two descriptor vectors
        angle_list = []
        # Step 4: Iterate over the list of 2nd descriptor vector
        for j in range(0, descriptors2.shape[0], 1):
            # Step 5: Find the cosine value between two descriptor vectors
            # descriptor1 ⋅ descriptor2 = |descriptor1||descriptor2| cos(angle)
            cosine_angle = np.dot(descriptors1[i], descriptors2[j])
            # Step 6: angle between two descriptor vectors
            angle = math.acos(cosine_angle)
            # Step 7: append the angle into list of angles
            angle_list.append(angle)
        # Step 8: list the index of angle values in ascending order
        index_list = np.argsort(angle_list)
        # Step 9: index of the best (smallest) angle
        best_match_index = index_list[0]
        # Step 10: index of the second best (smallest) angle
        second_best_match_index = index_list[1]
        # Step 11: Best angle
        best_angle = angle_list[best_match_index]
        # Step 12: Second best angle
        second_best_angle = angle_list[second_best_match_index]
        # Step 13: calculate the ratio between two angles
        ratio = np.abs(best_angle / second_best_angle)
        # Step 14: if ratio is below threshold, append to mathed pair list
        if ratio <= threshold:
            matched_pairs.append([i, best_match_index])
    # Step 15: return a list containing matched pairs
    return matched_pairs


# row in keypoints: x, y, scale, orientation
def RANSACFilter(matched_pairs: [[int, int]], keypoints1: np.ndarray, keypoints2: np.ndarray,
                 orient_agreement_in_degree: float, scale_agreement: float) -> [[int, int]]:
    assert isinstance(matched_pairs, list)
    assert isinstance(keypoints1, np.ndarray)
    assert isinstance(keypoints2, np.ndarray)
    assert isinstance(orient_agreement_in_degree, float)
    assert isinstance(scale_agreement, float)
    # Step1: Initialize largest subset
    largest_subset = []

    # Step2: Iterate 10 times
    for i in range(10):
        # Step3: Initialize consistency_set
        consistency_set = []
        # Step4: Select a random pair from matched_pairs
        selected_pair = random.choice(matched_pairs)

        # Step5: Calculate orientation difference of selected pair
        orientation1 = keypoints1[selected_pair[0]][3]
        orientation2 = keypoints2[selected_pair[1]][3]
        orient_difference = orientation2-orientation1

        # Step6: Convert to degree by multiplying 180°/π
        orient_difference = orient_difference*180.0/math.pi

        # Step7: Calculate scale proportion of selected pair
        scale1 = keypoints1[selected_pair[0]][2]
        scale2 = keypoints2[selected_pair[1]][2]
        scale_proportion = scale2/scale1

        # Step8: Iterate over all pairs in matched_pairs
        for current_pair in matched_pairs:
            # Step9: Calculate orientation difference of pair of current iteration
            orientation1_current_pair = keypoints1[current_pair[0]][3]
            orientation2_current_pair = keypoints2[current_pair[1]][3]
            current_pair_orient_difference = orientation2_current_pair-orientation1_current_pair
            # Step10: Convert to degree by multiplying 180°/π
            current_pair_orient_difference = current_pair_orient_difference*180.0/math.pi
            # Step11: clip orientation difference to [0°,360°)
            current_pair_orient_difference = current_pair_orient_difference % 360.0

            # Step12: Calculate scale proportion of pair of current iteration
            scale1_current_pair = keypoints1[current_pair[0]][2]
            scale2_current_pair = keypoints2[current_pair[1]][2]
            current_pair_scale_proportion = scale2_current_pair/scale1_current_pair

            # Step13: Check if current pair agree with selected pair's proportion requirement
            if (current_pair_scale_proportion < (1+scale_agreement)*scale_proportion):
                if (current_pair_scale_proportion > (1-scale_agreement)*scale_proportion):
                    # Step14: Check if current pair agree with selected pair's orientation requirement
                    if (current_pair_orient_difference < orient_difference+orient_agreement_in_degree):
                        if (current_pair_orient_difference > orient_difference-orient_agreement_in_degree):
                            # Step15: If all condition are met, append current pair to new_set
                            consistency_set.append(current_pair)

        # Step16: Find the largest set
        if len(consistency_set) > len(largest_subset):
            largest_subset = consistency_set

    assert isinstance(largest_subset, list)
    return largest_subset


# This is the same as transform matrix
def KeypointProjection(xy_points: np.ndarray, h: np.ndarray) -> np.ndarray:
    assert isinstance(xy_points, np.ndarray)
    assert isinstance(h, np.ndarray)
    assert xy_points.shape[1] == 2
    assert h.shape == (3, 3)

    # Step1: Transpose xy_points, so that it has (row: 2, column: N) shape
    xy_points = xy_points.T
    # Step2: Add a row with ones to xy_points
    row_of_ones = np.ones((1, xy_points.shape[1]), np.float64)
    xy_points = np.concatenate((xy_points, row_of_ones), axis=0)
    # Step3: dot product h to xy_points
    xy_points_out = np.dot(h, xy_points)
    # Step4: Divide first row and second row by third row
    xy_points_out = xy_points_out[:2]/xy_points_out[2]
    # Step5: Transpose back to original shape (row: N, column: 2)
    xy_points_out = xy_points_out.T

    return xy_points_out


def RANSACHomography(xy_src: np.ndarray, xy_ref: np.ndarray, num_iter: int, tol: float) -> np.ndarray:
    assert isinstance(xy_src, np.ndarray)
    assert isinstance(xy_ref, np.ndarray)
    assert xy_src.shape == xy_ref.shape
    assert xy_src.shape[1] == 2
    assert isinstance(num_iter, int)
    assert isinstance(tol, (int, float))
    tol = tol*1.0

    # current optimal homography matrix
    current_best_homography_matrix = np.zeros((3, 3))
    # number of inlier
    maximum_number_of_inlier = 0

    # Step1: iterate 'num_iter' times
    for round in range(num_iter):
        # Step2: randomly choose 4 matches from (x,y) list
        rows_of_selected_pair = np.random.choice(
            xy_src.shape[0], size=4, replace=False)
        # Step3: compute homography matrix using cv2.findHomography()
        homography_matrix, _ = cv2.findHomography(srcPoints=xy_src[rows_of_selected_pair],
                                                  dstPoints=xy_ref[rows_of_selected_pair], method=cv2.RANSAC)
        # Step4: project(transform) every (x,y) points in xy_src
        projected_xy_src = KeypointProjection(
            xy_points=xy_src, h=homography_matrix)

        # Step5: initialize(reset) number of inlier in this 4 pairs to 0
        number_of_inlier = 0

        # Step6: calculate Euclidean distance
        for i in range(xy_src.shape[0]):
            # x and y from projected xy_src
            x_projected_src = projected_xy_src[i][0]
            y_projected_src = projected_xy_src[i][1]
            # x and y from xy_ref
            x_ref = xy_ref[i][0]
            y_ref = xy_ref[i][1]
            # Step7: calculate Euclidean distance using l2 norm
            euclidean_distance = np.linalg.norm(
                np.array([x_projected_src - x_ref, y_projected_src - y_ref]))
            # Step8: count the number of inliers
            if (euclidean_distance < tol):
                number_of_inlier += 1
        # Step9: if number of inliers is larger than previous best homography matrix
        if (number_of_inlier > maximum_number_of_inlier):
            # Step10: update highest number of inliers
            maximum_number_of_inlier = number_of_inlier
            # Step11: update best homography matrix
            current_best_homography_matrix = homography_matrix

    h = current_best_homography_matrix

    assert isinstance(h, np.ndarray)
    assert h.shape == (3, 3)
    return h


def FindBestMatchesRANSAC(
        keypoints1, keypoints2,
        descriptors1, descriptors2, threshold,
        orient_agreement, scale_agreement):
    """
    Note: you do not need to change this function.
    However, we recommend you to study this function carefully
    to understand how each component interacts with each other.

    This function find the best matches between two images using RANSAC.
    Inputs:
        keypoints1, 2: keypoints from image 1 and image 2
            stored in np.array with shape (num_pts, 4)
            each row: row, col, scale, orientation
        descriptors1, 2: a K-by-128 array, where each row gives a descriptor
        for one of the K keypoints.  The descriptor is a 1D array of 128
        values with unit length.
        threshold: the threshold for the ratio test of "the distance to the nearest"
                   divided by "the distance to the second nearest neighbour".
                   pseudocode-wise: dist[best_idx]/dist[second_idx] <= threshold
        orient_agreement: in degrees, say 30 degrees.
        scale_agreement: in floating points, say 0.5
    Outputs:
        matched_pairs_ransac: a list in the form [(i, j)] where i and j means
        descriptors1[i] is matched with descriptors2[j].
    Detailed instructions are on the assignment website
    """
    orient_agreement = float(orient_agreement)
    assert isinstance(keypoints1, np.ndarray)
    assert isinstance(keypoints2, np.ndarray)
    assert isinstance(descriptors1, np.ndarray)
    assert isinstance(descriptors2, np.ndarray)
    assert isinstance(threshold, float)
    assert isinstance(orient_agreement, float)
    assert isinstance(scale_agreement, float)
    matched_pairs = FindBestMatches(
        descriptors1, descriptors2, threshold)
    matched_pairs_ransac = RANSACFilter(
        matched_pairs, keypoints1, keypoints2,
        orient_agreement, scale_agreement)
    return matched_pairs_ransac
