# Corner

- point where two edges intersect.

# Harris corner detection

1. Compute Harris 2nd moment matrix(Covariance matrix) $H$

$$ H= \begin{bmatrix} \sum (I_{x})^2 &&\sum I_{x} I_{y} \newline \sum I_{x}
I_{y} &&\sum (I_{y})^2 \end{bmatrix} $$

2. Compute two eigen values of $H$

$$
|H-\lambda|=0
$$

3. If $\lambda_{1}$ and $\lambda_{2}$ are similar, then image region has the corner.

# Harris corner detector

