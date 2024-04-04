# Template matching

| Notation | meaning                                           |
| -------- | ------------------------------------------------- |
| $I$      | Image region;where we find template               |
| $J$      | Template (filter)                                 |
| $\|I\|$  | Norm of image region; $\sqrt{\sum_{i} (J_{i})^2}$ |
| $\|J\|$  | Norm of template; $\sqrt{\sum_{i} (I_{i})^2}$     |

## Correlation

$$ CORR(I,J)=I^{T} J $$

- We need to maximize correlation between image region and template.

## Normalized correlation

$$ NCORR(I,J)=\frac{CORR(I,J)}{|I| |J|}=\frac{I^{T} J}{|I| |J|} $$

- By dividing correlation by norm, we are removing the factor affected by
  overall brightness difference between template and image region.
- **Large $NCRR(I,J)$ means the image region is highly similar to the
  template**.
- $NCRR(I,J)\in[-1,1]$
- $NCRR(I,J)=1$ means the image region and the template is identical.
- $NCRR(I,J)=0$ means there is no correlation between image region and template.

## Sum squared difference (SSD)

$$ SSD(I,J)=|I-J|^{2}=|I|^{2}+|J|^{2}-2CORR(I,J) $$

- **Low $SSD(I,J)$ means the image region is highly similar to the template**.

# Gradient $\nabla$

- Gradient of a function of one variable is simply its derivative.

| Notation                    | meaning                                                          |
| --------------------------- | ---------------------------------------------------------------- |
| $\nabla$                    | gradient;it is a vector                                          |
| $\frac{\delta f}{\delta x}$ | rate of change of $f$ with respect to $x$, holding $y$ constant. |
| $\frac{\delta f}{\delta y}$ | rate of change of $f$ with respect to $y$, holding $x$ constant. |

$$ \nabla f(x,y)=\begin{bmatrix} \frac{\delta f}{\delta x} \newline \frac{\delta
f}{\delta y} \end{bmatrix} $$

- Gradient of a function is a **vector which points at the greatest increasing
  direction from the point $(x,y)$**

# Laplacian $\nabla^{2}$

$$ \nabla^{2} f(x,y)= \frac{\delta^2 f}{\delta x^2}+\frac{\delta^2 f}{\delta
y^2} $$

- Laplacian is a scalar value.
- Laplacian represent the **rate of change of steepness at particular point**.
- If we calculate laplacian on gaussian filter, we can find edge.

# Laplacian of gaussian

$$ \nabla^{2} g(x,y)= \frac{\delta^2 g}{\delta x^2}+\frac{\delta^2 g}{\delta
y^2} $$

## steps to edge

1. Apply Gaussian filter to smooth the image.
2. Apply laplacian to smoothed image.
3. The point where the intensity is $0$, is the edge.
