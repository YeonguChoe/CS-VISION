# Reflection
## type
* Specular reflection (regular reflection)
* Lambertian reflection (diffuse reflection)

## Lambertian reflection

- Formula for how light interacts with rough surface leading to diffuse
  reflection.
- Intensity of reflected light doesn't depend on observer's viewpoint but only
  on the angle of incident light.

$$ I_{\text{diffuse reflection}}= k_{albedo} I_{\text{incident light}}
\cos{\theta} $$

- $I_{\text{diffuse}}$: intensity of diffuse reflected light
- $k_{\text{albedo}}$: diffuse reflectance coefficient of surface
- $I_{\text{incident light}}$: intensity of incident light
- $\theta$: angle between incident light and surface normal

## Specular reflection
- Phong model is extension of Lambertian model which includes both diffuse and
  specular reflection.

$$ I_{\text{specular}} = k_{\text{specular}} I_{\text{incident}}
\cos^{\alpha}{(\phi)} $$

- $I_{\text{specular}}$: intensity of specular reflection; unit: Watt/meter
- $k_{\text{specular}}$: specular reflection coefficient that determines amount
  that material reflects light; value between 0 and 1.
- $I_{\text{incident}}$: intensity of incident light on surface
- $\alpha$: shininess; determines the size of specular light; higher $\alpha$ results in
  smaller and focused highlight.
- $\phi$: angle between reflected light vector and the viewer's line of sight

# Perspective projection (pinhole camera)

| Denote     | Meaning                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| $f$        | focal length(pertaining to lens); when we say 50mm lens, it means the focal length is 50mm.           |
| full frame | projected image's length on image plane;when we say, 35mm lens, it means height of full frame is 35mm |
| $\theta$   | Field of view: Area captured by camera                                                                |

- If the sensor size is fixed, if focal length increase, field of view decrease
  making the image zoomed in.

## Camera matrix

$$ C=\begin{bmatrix} f' & 0 & 0 & 0\newline 0 & f' & 0 & 0\newline 0 & 0 & 1 & 0
\end{bmatrix} $$

- Camera matrix describes relationship between 3D world and 2D image plane.
- It is used to project 3D point into imagee plane.

## Projecting 3D object into 2D plane

$$ s P_{2d}=C P_{3d} $$

$$\text{3D object point } P_{3d}=\begin{bmatrix} x \newline y \newline z\newline
1 \end{bmatrix} $$

$$\text{2D object point } P_{2d}=\begin{bmatrix} x' \newline y' \newline 1
\end{bmatrix} $$

- scaling factor $s$ is the same as $z$.

## Summary of perspective projection

$$ x'={\frac{f'}{z}} {x} $$

$$ y'={\frac{f'}{z}} {y} $$

| Denote  | meaning                                    |
| ------- | ------------------------------------------ |
| $x',y'$ | projected image on 2D image plane          |
| $z$     | distance between camera lens and 3D object |

# Orthographic projection

- It is still a method to represent 3D object into 2D image plane.
- Projection lines are perpendicular to 2D image plane.
- Image projected on image plane has the same size as original object.

## Projecting 3D object into 2D plane

$$\text{3D object point } P_{3d}=\begin{bmatrix} x \newline y \newline z\newline
\end{bmatrix} $$

- We only take $x$ and $y$ from the 3D object point.

$$ \text{2D image point } P_{2d}=\begin{bmatrix} x \newline y \end{bmatrix} $$

# Weak perspective projection

- It is a simplified version of full perspective projection in that it uses
  constant scaling factor.
- Scaling factor is the same for all object.

## Projecting 3D object into 2D plane

- In weak perspective projection, the scailing factor $m$ is constant.

$$ \text{scailing factor}\ m=\frac{f'}{z_{0}} $$

- Therefore, we get

$$ x'=mx={\frac{f'}{z_0}} x $$

$$ y'=mx={\frac{f'}{z_0}} y $$

# Snell's law

| Denote       | meaning                                                               |
| ------------ | --------------------------------------------------------------------- |
| $\alpha_{1}$ | angle of incidence;ray of light that is approaching surface of object |
| $\alpha_{2}$ | angle of refraction                                                   |
| $n_{1}$      | refractive index value of material 1                                  |
| $n_{2}$      | refractive index value of material 2                                  |

$$ \frac{n_{2}}{n_{1}}=\frac{\sin{\alpha_{1}}}{\sin{\alpha{_{2}}}} $$

- Snell's law describes how light ray changes direction(bends) when passing from
  one material to another.
- Refractive index of material is **directly related to how fast light travels
  within that material compared light speed in vacuum**.

# Lens

| Notation    | meaning                                                                                                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| focal point | point where parallel ray of light from object at infinity converges after passing lens                                                                                                            |
| $f$         | focal length of lens;distance from center of lens to focal point;focal length of lens is **measured assuming the object is infinitely far** away from lens;focal length is fixed property of lens |
| $z$         | object distance;distance between center of lens to object                                                                                                                                         |
| $z'$        | image distance;distance between center of lens to image                                                                                                                                           |

## Thin lens formula

$$ \frac{1}{f}=\frac{1}{z}+\frac{1}{z'} $$

- Focal length $f$ is assuming the ray is coming from infinitely far object, so
  we can assume $\frac{1}{f}$ is a fixed constant.
- Therefore, the thin lens formula is about **relationship between object
  distance $z$ and image distance $z'$**.

# Vignetting

- Gradual decrease of brightness or saturation of image toward edges.

# Spherical Aberration

- Reduction of image sharpness due to imperfect shape of lens.
- Lens does not focus incidence light ray to a single point.

# Chromatic Aberration

- Refractive index depends on the wavelength $(\lambda)$ of light. Therefore,
  different colors in light have different refraction angle.
- Color distortion happens in chromatic aberration.
