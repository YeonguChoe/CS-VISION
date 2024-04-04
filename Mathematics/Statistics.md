# Statistics

## Correlation

### Symbol of correlation

$$
\otimes
$$

### Meaning of correlation

* Correlation measures the extent of similarity between image and filter.
* Correlation calculates the similarity score by sliding filter over image.
* Correlation is used in template matching which find the specific area within the image.

### Correlation formula in computer science

$$
I_{Correlation}(X,Y)=\sum_{j=-k}^k \sum_{i=-k}^k F(i,j)I(X+i,Y+j)
$$

* $F$ is the filter.
* $I$ is the image.
* $X$ and $Y$ is the pixel intensity of original image positioned at the center of filter.
* $i$ and $j$ is the coordinate on filter.

## Cross-correlation

### Formula of Cross-correlation

$$
\frac{1}{n} \sum_{x,y}\frac{1}{\sigma_f \sigma_t} f(x,y) t(x,y
$$

### Meaning of Cross-correlation
* Cross-correlation is a measure of similarity of two signals as a function.
* We slide dot product over image.

### Comparison with correlation
* Normal correlation can be used to find patterns in images, while cross-correlation can be used to find specific features in images.
* Cross correlation use weighted sum.

## Convolution
* Convolution is a mathematical operation that takes two functions and produces a third function.
* Inputs of convolution operation are stationary function $f(x)$ and moving function $h(x)$.

* Etymology of convolution is "state of being rolled upon itself".
* A convolution of $f(x)$ and $g(x)$ is the overlapping part with $f(x)$, when moving $g(x)$.

### Convolution Formula in Mathematics
* In RHS, $-\tau$ means reflection through y axis.
* $+x$ means moving $-x$ amount to x axis.
#### 1 dimensional convolution
$$
g(x) = f(x)*h(x)=\int_{-\infty}^{\infty} f(\tau)h(-\tau+x)d\tau
$$

#### 2 dimensional convolution
* $f$ is the intensity of pixel.
* $h$ is the filter.

$$
g(x,y) = f(x,y)*h(x,y)=\iint_{-\infty}^{\infty} f(\tau,\mu)h(-\tau-(-x), -\mu-(-y))d\tau d\mu
$$
        
#### Convolution formula in Computer science
* $x$ and $y$ is a coordination of a pixel.
* The size of a filter is $R(width)\times R(height)$.
* $g(x,y)$ is a new intensity of the pixel.

$$
g(x,y)=f(x,y)*h(x,y)=\sum_{\tau=1}^{R} \sum_{\mu=1}^{R} f(\tau,\mu)\cdot h(-\tau-(-x),-\mu-(-y))
$$