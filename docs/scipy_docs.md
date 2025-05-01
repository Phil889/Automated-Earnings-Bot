# SciPy Documentation: Interpolation

This document contains code snippets and examples for using SciPy's interpolation functionality, which is relevant for the Automated Earnings Bot project, particularly for building the IV term structure spline.

## 1D Interpolation

### Basic Linear Interpolation

```python
import numpy as np
from scipy.interpolate import interp1d

# Create sample data
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

# Create linear interpolation function
f = interp1d(x, y)

# Create cubic interpolation function
f2 = interp1d(x, y, kind='cubic')

# Evaluate at new points
xnew = np.linspace(0, 10, num=41, endpoint=True)

# Plot results
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
```

### Nearest, Previous, and Next Interpolation

```python
from scipy.interpolate import interp1d

# Create sample data
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

# Create interpolation functions
f1 = interp1d(x, y, kind='nearest')
f2 = interp1d(x, y, kind='previous')
f3 = interp1d(x, y, kind='next')

# Evaluate at new points
xnew = np.linspace(0, 10, num=1001, endpoint=True)

# Plot results
import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
plt.plot(xnew, f1(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew), ':')
plt.legend(['data', 'nearest', 'previous', 'next'], loc='best')
plt.show()
```

### Cubic Spline Interpolation

```python
from scipy.interpolate import CubicSpline

# Create and evaluate a cubic spline
spl = CubicSpline([1, 2, 3, 4, 5, 6], [1, 4, 8, 16, 25, 36])
spl(2.5)  # Evaluate at x=2.5
```

### Comparing CubicSpline Boundary Conditions

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Sample data
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [4.5, 3.6, 1.6, 0.0, -3.3, -3.1, -1.8, -1.7]

# Create splines with different boundary conditions
notaknot = CubicSpline(xs, ys, bc_type='not-a-knot')
natural = CubicSpline(xs, ys, bc_type='natural')
clamped = CubicSpline(xs, ys, bc_type='clamped')

# Evaluate at new points
xnew = np.linspace(min(xs) - 4, max(xs) + 4, 101)

# Plot splines and their derivatives
splines = [notaknot, natural, clamped]
titles = ['not-a-knot', 'natural', 'clamped']

fig, axs = plt.subplots(3, 3, figsize=(12, 12))
for i in [0, 1, 2]:  # Plot function and first two derivatives
    for j, spline, title in zip(range(3), splines, titles):
        axs[i, j].plot(xs, spline(xs, nu=i),'o')
        axs[i, j].plot(xnew, spline(xnew, nu=i),'-')
        axs[i, j].set_title(f'{title}, deriv={i}')
        
plt.tight_layout()
plt.show()
```

### Extending CubicSpline for Custom Extrapolation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def add_boundary_knots(spline):
    """
    Add knots infinitesimally to the left and right.

    Additional intervals are added to have zero 2nd and 3rd derivatives,
    and to maintain the first derivative from whatever boundary condition
    was selected. The spline is modified in place.
    """
    # determine the slope at the left edge
    leftx = spline.x[0]
    lefty = spline(leftx)
    leftslope = spline(leftx, nu=1)

    # add a new breakpoint just to the left and use the
    # known slope to construct the PPoly coefficients.
    leftxnext = np.nextafter(leftx, leftx - 1)
    leftynext = lefty + leftslope*(leftxnext - leftx)
    leftcoeffs = np.array([0, 0, leftslope, leftynext])
    spline.extend(leftcoeffs[..., None], np.r_[leftxnext])

    # repeat with additional knots to the right
    rightx = spline.x[-1]
    righty = spline(rightx)
    rightslope = spline(rightx,nu=1)
    rightxnext = np.nextafter(rightx, rightx + 1)
    rightynext = righty + rightslope * (rightxnext - rightx)
    rightcoeffs = np.array([0, 0, rightslope, rightynext])
    spline.extend(rightcoeffs[..., None], np.r_[rightxnext])

# Sample data
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [4.5, 3.6, 1.6, 0.0, -3.3, -3.1, -1.8, -1.7]

# Create splines with different boundary conditions
notaknot = CubicSpline(xs, ys, bc_type='not-a-knot')
natural = CubicSpline(xs, ys, bc_type='natural')
clamped = CubicSpline(xs, ys, bc_type='clamped')

# Extend the natural and clamped splines
add_boundary_knots(natural)
add_boundary_knots(clamped)
```

### Batch Interpolation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Create sample data with multiple functions
n = 11
x = 2 * np.pi * np.arange(n) / n
y = np.stack((np.sin(x)**2, np.cos(x)), axis=1)

# Create spline for batch interpolation
spl = make_interp_spline(x, y)

# Evaluate at new points
xv = np.linspace(0, 2*np.pi, 51)

# Plot results
plt.plot(x, y, 'o')
plt.plot(xv, spl(xv), '-')
plt.show()
```

### Different Parametrizations for Curve Interpolation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Sample data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 0, 0, 9, 0, 0, 0]
p = np.stack((x, y))

# Uniform parametrization
u_unif = x

# Cord length parametrization
dp = p[:, 1:] - p[:, :-1]      # 2-vector distances between points
l = (dp**2).sum(axis=0)        # squares of lengths of 2-vectors between points
u_cord = np.sqrt(l).cumsum()   # cumulative sums of 2-norms
u_cord = np.r_[0, u_cord]      # the first point is parameterized at zero

# Centripetal parametrization
u_c = np.r_[0, np.cumsum((dp**2).sum(axis=0)**0.25)]

# Plot results
fig, ax = plt.subplots(1, 3, figsize=(8, 3))
parametrizations = ['uniform', 'cord length', 'centripetal']

for j, u in enumerate([u_unif, u_cord, u_c]):
   spl = make_interp_spline(u, p, axis=1)    # note p is a 2D array
   
   uu = np.linspace(u[0], u[-1], 51)
   xx, yy = spl(uu)
   
   ax[j].plot(xx, yy, '--')
   ax[j].plot(p[0, :], p[1, :], 'o')
   ax[j].set_title(parametrizations[j])
plt.show()
```

## 2D Interpolation

### Griddata Interpolation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Sample data (scattered points)
points = np.random.rand(100, 2)
values = np.sin(points[:,0] * 10) + np.cos(points[:,1] * 10)

# Define grid for interpolation
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Interpolate using different methods
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

# Plot results
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(grid_z0, extent=(0,1,0,1), origin='lower')
plt.title('Nearest')
plt.subplot(132)
plt.imshow(grid_z1, extent=(0,1,0,1), origin='lower')
plt.title('Linear')
plt.subplot(133)
plt.imshow(grid_z2, extent=(0,1,0,1), origin='lower')
plt.title('Cubic')
plt.gcf().tight_layout()
plt.show()
```

### Custom 2D Interpolation with Nearest-Neighbor Extrapolation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CloughTocher2DInterpolator as CT

def my_CT(xy, z):
    """CT interpolator + nearest-neighbor extrapolation.

    Parameters
    ----------
    xy : ndarray, shape (npoints, ndim)
        Coordinates of data points
    z : ndarray, shape (npoints)
        Values at data points

    Returns
    -------
    func : callable
        A callable object which mirrors the CT behavior,
        with an additional neareast-neighbor extrapolation
        outside of the data range.
    """
    x = xy[:, 0]
    y = xy[:, 1]
    f = CT(xy, z)

    # this inner function will be returned to a user
    def new_f(xx, yy):
        # evaluate the CT interpolator. Out-of-bounds values are nan.
        zz = f(xx, yy)
        nans = np.isnan(zz)

        if nans.any():
            # for each nan point, find its nearest neighbor
            inds = np.argmin(
                (x[:, None] - xx[nans])**2 +
                (y[:, None] - yy[nans])**2
                , axis=0)
            # ... and use its value
            zz[nans] = z[inds]
        return zz

    return new_f

# Example usage
x = np.array([1, 1, 1, 2, 2, 2, 4, 4, 4])
y = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
z = np.array([0, 7, 8, 3, 4, 7, 1, 3, 4])

xy = np.c_[x, y]
lut = CT(xy, z)
lut2 = my_CT(xy, z)

X = np.linspace(min(x) - 0.5, max(x) + 0.5, 71)
Y = np.linspace(min(y) - 0.5, max(y) + 0.5, 71)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(X, Y, lut(X, Y), label='CT')
ax.plot_wireframe(X, Y, lut2(X, Y), color='m',
                  cstride=10, rstride=10, alpha=0.7, label='CT + n.n.')

ax.scatter(x, y, z,  'o', color='k', s=48, label='data')
ax.legend()
plt.tight_layout()
plt.show()
```

## Extrapolation Techniques

### Replicating numpy.interp behavior with scipy.interpolate.interp1d

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Sample data
x = np.linspace(0, 1.5*np.pi, 11)
y = np.column_stack((np.cos(x), np.sin(x)))   # y.shape is (11, 2)

# Create interpolation function with extrapolation
func = interp1d(x, y,
                axis=0,  # interpolate along columns
                bounds_error=False,
                kind='linear',
                fill_value=(y[0], y[-1]))

# Evaluate at points outside the original range
xnew = np.linspace(-np.pi, 2.5*np.pi, 51)
ynew = func(xnew)

# Plot results
fix, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.plot(xnew, ynew[:, 0])
ax1.plot(x, y[:, 0], 'o')

ax2.plot(xnew, ynew[:, 1])
ax2.plot(x, y[:, 1], 'o')
plt.tight_layout()
plt.show()
```

### Inverse Interpolation with Derivatives

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BPoly

def f(x, a):
    return a*x - 1/np.tan(x)

# Sample data
xleft, xright = 0.2, np.pi/2
x = np.linspace(xleft, xright, 11)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))

for j, a in enumerate([3, 93]):
    y = f(x, a)
    dydx = a + 1./np.sin(x)**2    # d(ax - 1/tan(x)) / dx
    dxdy = 1 / dydx               # dx/dy = 1 / (dy/dx)

    # Inverse interpolation with derivatives
    xdx = np.c_[x, dxdy]
    spl = BPoly.from_derivatives(y, xdx)   # inverse interpolation

    # Evaluate and plot
    yy = np.linspace(f(xleft, a), f(xright, a), 51)
    ax[j].plot(yy, spl(yy), '--')
    ax[j].plot(y, x, 'o')
    ax[j].set_xlabel(r'$y$')
    ax[j].set_ylabel(r'$x$')
    ax[j].set_title(rf'$a = {a}$')

    ax[j].plot(0, spl(0), 'o', ms=12)
    ax[j].text(0.1, 0.85, fr'$x_0 = {spl(0):.3f}$',
               transform=ax[j].transAxes, fontsize=18)
    ax[j].grid(True)
plt.tight_layout()
plt.show()
```

## Spline Interpolation for IV Term Structure

For the Automated Earnings Bot project, we need to build an IV term structure spline. Here's an example of how to do this using SciPy's interpolation functionality:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def build_term_structure(expiries, ivs):
    """
    Build a term structure spline from expiry dates and implied volatilities.
    
    Parameters:
    -----------
    expiries : array-like
        Array of expiry dates in days to expiration
    ivs : array-like
        Array of implied volatilities corresponding to each expiry
        
    Returns:
    --------
    spline : CubicSpline
        A cubic spline interpolator for the IV term structure
    """
    # Sort by expiry if not already sorted
    idx = np.argsort(expiries)
    expiries = np.array(expiries)[idx]
    ivs = np.array(ivs)[idx]
    
    # Create cubic spline with natural boundary conditions
    # (second derivative is zero at endpoints)
    spline = CubicSpline(expiries, ivs, bc_type='natural')
    
    return spline

# Example usage
expiries = np.array([7, 14, 30, 60, 90, 180, 270, 365])  # days to expiration
ivs = np.array([0.25, 0.24, 0.22, 0.21, 0.20, 0.19, 0.18, 0.18])  # implied volatilities

# Build the term structure spline
iv_spline = build_term_structure(expiries, ivs)

# Evaluate at new points
new_expiries = np.linspace(0, 400, 100)
new_ivs = iv_spline(new_expiries)

# Plot the term structure
plt.figure(figsize=(10, 6))
plt.plot(expiries, ivs, 'o', label='Market IVs')
plt.plot(new_expiries, new_ivs, '-', label='IV Term Structure')
plt.xlabel('Days to Expiration')
plt.ylabel('Implied Volatility')
plt.title('IV Term Structure')
plt.grid(True)
plt.legend()
plt.show()
