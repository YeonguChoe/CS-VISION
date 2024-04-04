# Intensity

- In Grayscale image, intensity is single value between 0~255.
  - If the intensity is 0, the image is black.
- In RGB Color model, each red, green and blue have intensity between 0~255.
  - Hexadecimal value represents RGB values of RGB color model.
- In HSL Color model, the saturation value between 0%~100% is the intensity.
  However, in computer science, color image mostly use RGB color model than HSL
  color model.

# Image as function

- $I(x,y)$ represents the intensity value of each pixel.
- For color image, there are RGB pixel value for each $I_{R}(x,y),\ I_{G}(x,y)$
  and $I_{B}(x,y)$.

* Range of image function

$$ I(X,Y)\in [0,255] $$

# Correlation

| Notation     | meaning                                       |
| ------------ | --------------------------------------------- |
| $i$          | column of filter matrix(kernel)               |
| $j$          | row of filter matrix(kernel)                  |
| $f(i,j)$     | filter value at $(i,j)$                       |
| $I(x+i,y+j)$ | intensity of the pixel located at $(x+i,y+j)$ |
| $\odot$      | correlation symbol                            |

$$ I_{correlation}(x,y)=(I\odot f)(x,y)=\sum_{i} \sum_{j} I(x+i,y+j)f(i,j) $$

- ${I}_{correlation}(x,y)$ is the new intensity of pixel located at $(x,y)$.
- $x+i$ means translating $x$ by $-i$ units to $x$ direction.
- $y+j$ means translating $y$ by $-j$ units to $y$ direction.
- Time complexity: $O\left((\text{size of filter})^{4}\right)$

# Convolution

| Notation     | meaning                                       |
| ------------ | --------------------------------------------- |
| $i$          | column of filter matrix(kernel)               |
| $j$          | row of filter matrix(kernel)                  |
| $f(i,j)$     | filter value at $(i,j)$                       |
| $I(x-i,y-j)$ | intensity of the pixel located at $(x-i,y-j)$ |
| $\ast$       | convolution symbol                            |

$$ I_{convolution}(x,y)=(I\ast f)(x,y)=\sum_{i} \sum_{j} I(x-i,y-j)f(i,j) $$

- **We use convolution instead of correlation because of mathematical
  property(Communitativity: $f\ast g=g\ast f$)**
- $ij$ represent number of cells within the kernel.
- Filter of image processing is designed to fit convolution.

* ${I}_{convolution}(x,y)$ is the new intensity of pixel located at $(x,y)$.
* $x-i$ means translating $x$ by $+i$ units to $x$ direction.
* $y-j$ means translating $y$ by $+j$ units to $y$ direction.

## 1D Convolution as matrix multiplication

- filter:

$$ \begin{bmatrix} 1 & 2 & 1 \end{bmatrix} $$

- image:

$$ \begin{bmatrix} 78 & 88 & 62 & 52 & 37 \end{bmatrix} $$

### Matrix multiplication

1. include 0 to the beginning and the end of image matrix and take transpose

$$ \begin{bmatrix} 0\newline78\newline88\newline62\newline52\newline37\newline 0
\end{bmatrix} $$

2. Do the **matrix multiplication** and **divide by sum of all the values in the
   filter**

$$ {\frac{1}{(1+2+1)}} \begin{bmatrix} 1&2&1&0&0&0&0\newline
0&1&2&1&0&0&0\newline 0&0&1&2&1&0&0\newline 0&0&0&1&2&1&0&\newline
0&0&0&0&1&2&1\newline \end{bmatrix} \begin{bmatrix} 0\newline 78\newline
88\newline 62\newline 52\newline 37\newline 0 \end{bmatrix} $$

# Property

| Operation   | Communitativity $(xy=yx)$ | Associativity $(x(yz)=(xy)z)$            | Distributivity $x(y+z)=xy+xz$            |
| ----------- | ------------------------- | ---------------------------------------- | ---------------------------------------- |
| Correlation | No                        | No                                       | No                                       |
| Convolution | Yes; $(f\ast g=g\ast f)$  | Yes; $(f\ast (g\ast h)=(f\ast g)\ast h)$ | Yes; $(f\ast (g+h)=(f\ast g)+(f\ast h))$ |

# Gaussian filter

| Notation | meaning            |
| -------- | ------------------ |
| $\sigma$ | standard deviation |

## 1D Gaussian filter

$$ G(x)=\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{1}{2} (\frac{x}{\sigma})^2} $$

$$ G(y)=\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{1}{2} (\frac{y}{\sigma})^2} $$

## 2D Gaussian filter

$$ G(x,y)=\frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}} $$

- Standard deviation $\sigma$ controls the spread of gaussian distribution.
  - High $\sigma$ gives stronger blurring of image.
- Kernel size decides the extent that gaussian filter is applied.
- 2D Gaussian filter can be expressed as product of $G(x)$ and $G(y)$.

* 2D Gaussian filter can be seperated into two 1D Guassian filter, so Gaussian
  filter is seperable.

$$ G(x,y)=G(x)G(y) $$

# Median filter

1. Sort intensity values within the kernel in ascending order.
2. Pick the intensity value in the middle, which is $\frac{n+1}{2}th$ value.

# Linear filter

- In order for a filter to be a linear, the filter needs to satisfy two
  conditions.

## Condition 1: Additivity

- The result of filter on summation of inputs is the same as the summation of
  results of filter on each input.

$$ Filter(input_{1}+input_{2})=Filter(input_{1})+Filter(input_{2}) $$

## Condition 2: Homogeneity

- The result of filter on scaled input is the same as scaling on the result of
  filter on input.

$$ Filter(c\cdot input)=c\cdot Filter(input) $$

## Categorization

| Linear filter         | Non-linear filter |
| --------------------- | ----------------- |
| Correlation           | Median filter     |
| Convolution           | Bilateral filter  |
| Gaussian filter       | ReLu              |
| Laplacian of Gaussian |                   |

# Inner product(dot product)

- Inner product is the same as dot product.
- The result of inner product is a scalar.

## Inner product of $a$ and $b$

- Given

$$ a=\begin{bmatrix} a_{1}\newline a_{2}\newline a_{3} \end{bmatrix} $$

$$ b=\begin{bmatrix} b_{1}\newline b_{2}\newline b_{3} \end{bmatrix} $$

- Inner product of $a$ and $b$

$$ a\cdot b=a^{T} b=\begin{bmatrix} a_{1}&& a_{2}&& a_{3} \end{bmatrix}
\begin{bmatrix} b_{1}\newline b_{2}\newline b_{3} \end{bmatrix} $$

# Outer product

- The result of outer product is a matrix.
- Outer product is different from cross product.

## Outer product of $a$ and $b$

- Given

$$ a=\begin{bmatrix} a_{1}\newline a_{2}\newline a_{3} \end{bmatrix} $$

$$ b=\begin{bmatrix} b_{1}\newline b_{2}\newline b_{3} \end{bmatrix} $$

- Inner product of $a$ and $b$

$$ a\otimes b=ab^{T}= \begin{bmatrix} b_{1}\newline b_{2}\newline b_{3}
\end{bmatrix} \begin{bmatrix} a_{1}&& a_{2}&& a_{3} \end{bmatrix}$$

# Seperable filter

- In order for a filter to be seperable, the filter needs to satisfy following
  condition.

## Condition: outer product of two 1D filters

- The 2D filter can be decomposed into two 1D filters.
- The 2D filter is the outer product of two 1D filters.

$$ Filter=Filter_{1}\otimes Filter_{2} $$

## Categorization

| Seperable filter     | Non-seperable filter  |
| -------------------- | --------------------- |
| (2D) Gaussian filter | Correlation           |
|                      | Convolution           |
|                      | Bilateral filter      |
|                      | Laplacian of gaussian |

# Rotationally invariant filter

- Rotationally invariant filter perform the same and output the same result,
  although the filter is rotated.

## Categorization

| Rotationally invariant filter | Non-rotationally invariant filter |
| ----------------------------- | --------------------------------- |
| Convolution                   | Correlation                       |
| (2D) Gaussian filter          | Median filter                     |
| Bilateral filter              |                                   |
| Laplacian of gaussian         |                                   |
