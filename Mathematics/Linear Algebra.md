# Linear algebra

## Eigenvalue and Eigenvector


If we have a $n\times n$ matrix $A$ as an input,

$$ \begin{bmatrix} a&b\newline c&d \end{bmatrix} $$

Eigenvector is a special vector when it is multiplied to $A$, the vector
   $\vec{x}$ does not choose direction. However, it can be stretched by
   $\lambda$ multiple.

$$ A \vec{x}=\begin{bmatrix} a&b\newline c&d \end{bmatrix}=\lambda\vec{x} $$

- $\vec{x}$: Eigenvector of matrix $A$
- $\lambda$: Eigenvalue of matrix $A$

## Determinant

### Meaning of determinant

1. Solvability of linear system: In $AX=B$, where $A$ is a square matrix, the
   system has a unique solution if and only if $det \left (A \right )$ is not
   $0$.
1. Invertibility: A square matrix can have inverse matrix if and only if its
   determinant is not $0$.
1. Area/volume scaling factor: A determinant value of a square matrix is how
   much area will be factored.

$$ det \left(A_{2D} \right)=\frac{area_{new\ A}}{area_{old\ A}} $$

$$ det \left(A_{3D} \right)=\frac{volume_{new\ A}}{volume_{old\ A}} $$

### Things to consider
- If $det(A)<0$, then orientation of shape is inverted.

### 2D determinant formula

$$ det\left (\begin{bmatrix} a&b \newline c&d \newline \end{bmatrix}\right ) =
ad-bc $$

### 3D determinant formula

$$ det\left (\begin{bmatrix} a&b&c\newline d&e&f\newline g&h&i
\end{bmatrix}\right ) = a(ei-fh)-b(di-fg)+c(dh-eg) $$

## Inverse matrix

$$ A^{-1}A=AA^{-1}=\begin{bmatrix} 1&0 \newline 0&1 \end{bmatrix} $$

### 2 Dimensional matrix

$$ {\begin{bmatrix}a&b \newline c&d \end{bmatrix}}^{-1}=\frac{1}{ad-bc}
\begin{bmatrix} d&-b \newline -c&a \end{bmatrix} $$

## Dot product

### Meaning of dot product
1. Geometric interpretation: Dot product of two vectors is the extent to which they are pointing to the same direction. If the dot product is positive, they are pointing to the similar direction. If the dot product is negative, they are pointing to the opposite direction.

### Things to consider
- Dot product is an operation between two matrices. And the result is scalar.
- Note that dot product is different from matrix multiplication

### Dot product of two vectors

$$ \left\langle \begin{matrix} a & b & c \end{matrix}
\right\rangle\cdot\left\langle \begin{matrix} d & e & f\end{matrix}
\right\rangle=ad+be+cf $$

## Cross product

### Meaning of cross product
1. Perpendicular vector: The cross product of two vectors is a vector pointing at the perpendicular direction of two vectors based on right hand rule.
1. Area of parallelogram: The magnitude of cross product of two vectors is the area of parallelogram.

$$
\left |A\times B \right |
$$

### Things to consider
- Cross product is an operation between two matrices, which returns vector.

### Cross product of two vectors

$$\left\langle \begin{matrix} a & b & c \end{matrix} \right\rangle \times
\left\langle \begin{matrix} d & e & f \end{matrix} \right\rangle=\begin{vmatrix}
i&j&k\newline a & b & c\newline d&e&f\newline \end{vmatrix}=det \left (
\begin{bmatrix} b&c\newline e&f\newline\end{bmatrix} \right )i+det \left (
\begin{bmatrix} a&c\newline d&f\newline\end{bmatrix} \right )j+det \left (
\begin{bmatrix} a&b\newline d&e\newline\end{bmatrix} \right )k
=(bf-cd)i+(af-cd)j+(ae-bd)k$$

## Transpose

$$ \begin{bmatrix} a&e\newline b&f\newline c&g\end{bmatrix}^T=\begin{bmatrix}
a&b&c\newline d&e&f\newline\end{bmatrix} $$
