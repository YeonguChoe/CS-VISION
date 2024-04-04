# SIFT(Scale invariant feature transform)

- Idea: find and match interest point(same feature)

| Vocab          | meaning                                                         |
| -------------- | --------------------------------------------------------------- |
| interest point | a point in an image that has distinctive feature                |
| blob           | group of adjacent pixels in image that have similar intensity   |
| Detector       | identify key interest points in an image, and output blob       |
| Descriptor     | encode information of interest point and its blob into a vector |

# RANSAC(Random sample consensus)

| Notation | meaning                                                                          |
| -------- | -------------------------------------------------------------------------------- |
| Outlier  | match between two points in two images, that are actually different; false match |

- SIFT sometimes find incorrect matches between two images.
- RANSAC algorithm is used to remove these false matches.
- Randomly choose two points, and draw line. Count the dots on the line. Iterate
  this step until finding a line with the most dots(inliers).

# K-means clustering

- it is an algorithm that group data points into k clusters.
- The output of k-mean clustering is a set of sets, which is clusters.
- K-mean clustering algorithm minimize the total within-cluster variance.

| Notation                              | meaning                                                               |
| ------------------------------------- | --------------------------------------------------------------------- |
| $\underset{x}{\text{arg min}\ } f(x)$ | argument of minimum;argument that makes the function $f$ into minimum |
| $S_{i}$                               | $i^{th}$ cluster                                                      |
| $S$                                   | set of clusters                                                       |
| $\mu_{i}$                             | mean of points in a set $S_i$                                         |

$$ \text{mean }\mu_{i}=\frac{1}{|S_{i}|} \sum_{x\in S_{i}} x $$

$$ \text{K-mean clustering}=\underset{S}{\text{arg min}\ } \sum_{S_{i}\in S}
\sum_{x\in S_{i}} {||x-\mu_{S_{i}} ||}^2 $$

# Support vector machine(SVM)

| Word                   | meaning                                                                     |
| ---------------------- | --------------------------------------------------------------------------- |
| Decision boundary      | hypothetical boundary that separates clusters; it is also called hyperplane |
| Margin                 | distance between decision boundary and closest points of a cluster          |
| Support vector         | points that are closest to the decision boundary                            |
| Support vector machine | SVM is an algorithm to find decision boundary that has the largest margin.  |

# Terminology

| Term       | meaning                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------ |
| Classifier | Algorithm that categorizes points into categories $\text{point}\rightarrow \text{cluster}$ |
| Label      | specific value that is assigned to a point                                                 |

# Nearest mean classifier

## Training step

- Compute mean for each category using training data.

## Prediction step

- Compute difference with means categories.
- Then, put the point into the category with the minimum difference.

$$ \text{category of x}=\text{arg } \underset{i}{\text{min }} |x-\mu_{i}|^2 $$

# K Nearest Neighbor(KNN) classifier

1. Calculate the distance between input point and all the other points in
   categories.
2. Sort the distance in ascending order
3. Make a set out of the first $k$ points which have close distance with input
   point
4. Select the category with the most common points in the set

# Cross validation
