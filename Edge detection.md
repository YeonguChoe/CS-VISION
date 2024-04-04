# Edge
Rapid change in intensity within small region

# Edge detection

1. Smooth(reduce noise) the original image with a Gaussian filter.

$$ G\ast I (x,y) $$

2. Take gradient of smoothed image.

$$ \nabla (G\ast I(x,y)) $$

3. The local extrema is the edge.

# Sobel edge detector
* 1-2-1 matrix represent the gaussian filter. 1-2-1 is the weight.
* (-1)-(+1)-(-1) matrix represent the central derivative.

## Sobel X filter

$$ \begin{bmatrix} 1 \newline 2 \newline 1 \end{bmatrix} \begin{bmatrix} -1 && 0
&& 1 \end{bmatrix}= \begin{bmatrix} -1&0&1 \newline -2&0&2 \newline -1&0&1
\end{bmatrix} $$

## Sobel Y filter

$$ \begin{bmatrix} -1 \newline 0 \newline 1 \end{bmatrix} \begin{bmatrix} 1 && 2
&& 1 \end{bmatrix}= \begin{bmatrix} -1&-2&1 \newline 0&0&0 \newline 1&2&1
\end{bmatrix} $$

# Canny edge detector

1. Smooth the original image with Gaussian filter

$$ G\ast I(x,y) $$

2. Compute the gradient

$$ \nabla (G\ast I(x,y)) $$

3. Compute the gradient magnitude

$$ ||\nabla (G\ast I(x,y))||=\sqrt{\left(\frac{\delta G\ast I}{\delta
x}\right)^2+\left(\frac{\delta G\ast I}{\delta y}\right)^2} $$

4. Compute gradient direction

- We divide it by gradient magnitude to make an unit vector.

$$ \vec{n}=\frac{\nabla (G\ast I(x,y))}{||\nabla (G\ast I(x,y))||} $$

5. Take laplacian with respect to the gradient direction

$$ \frac{\delta^{2} G\ast I(x,y)}{\delta \vec{n}^2} $$

6. The zero crossing region is the edge.
