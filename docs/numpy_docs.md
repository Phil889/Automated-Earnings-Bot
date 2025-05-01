# NumPy Documentation: Numerical Operations and Array Manipulations

This document contains code snippets and examples for using NumPy for numerical operations and array manipulations, which are relevant for the Automated Earnings Bot project.

## Creating Arrays

### Basic Array Creation

```python
import numpy as np

# Create an array from a list
arr = np.array([1, 2, 3, 4, 5])

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create an array of zeros
zeros = np.zeros((3, 4))  # 3x4 matrix of zeros

# Create an array of ones
ones = np.ones((2, 3))  # 2x3 matrix of ones

# Create an identity matrix
identity = np.eye(3)  # 3x3 identity matrix

# Create an array with a range of values
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Create an array with evenly spaced values
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
```

### Random Number Generation

```python
# Set random seed for reproducibility
np.random.seed(42)

# Generate random numbers from a uniform distribution
uniform = np.random.rand(3, 3)  # 3x3 matrix of random values between 0 and 1

# Generate random integers
integers = np.random.randint(0, 10, size=(3, 3))  # 3x3 matrix of random integers between 0 and 10

# Generate random numbers from a normal (Gaussian) distribution
normal = np.random.randn(3, 3)  # 3x3 matrix of random values from standard normal distribution

# Generate random numbers from a normal distribution with specified mean and standard deviation
normal_custom = np.random.normal(loc=0.0, scale=1.0, size=(3, 3))
```

## Array Operations

### Basic Operations

```python
# Element-wise addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b  # [5, 7, 9]

# Element-wise subtraction
d = b - a  # [3, 3, 3]

# Element-wise multiplication
e = a * b  # [4, 10, 18]

# Element-wise division
f = b / a  # [4.0, 2.5, 2.0]

# Element-wise power
g = a ** 2  # [1, 4, 9]

# Matrix multiplication
h = np.dot(a, b)  # 32 (dot product)
```

### Array Manipulation

```python
# Reshape an array
a = np.arange(12)  # [0, 1, 2, ..., 11]
b = a.reshape(3, 4)  # 3x4 matrix

# Transpose a matrix
c = b.T  # 4x3 matrix

# Flatten an array
d = b.flatten()  # [0, 1, 2, ..., 11]

# Concatenate arrays
e = np.concatenate((a, a))  # [0, 1, ..., 11, 0, 1, ..., 11]

# Stack arrays vertically
f = np.vstack((b, b))  # 6x4 matrix

# Stack arrays horizontally
g = np.hstack((b, b))  # 3x8 matrix

# Split an array
h = np.split(a, 3)  # List of 3 arrays, each with 4 elements
```

### Broadcasting

```python
# Broadcasting allows NumPy to work with arrays of different shapes
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
c = a + b  # 3x3 matrix: [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
```

## Statistical Functions

```python
a = np.array([1, 2, 3, 4, 5])

# Mean
mean = np.mean(a)  # 3.0

# Median
median = np.median(a)  # 3.0

# Standard deviation
std = np.std(a)  # ~1.41

# Variance
var = np.var(a)  # 2.0

# Min and max
min_val = np.min(a)  # 1
max_val = np.max(a)  # 5

# Sum
sum_val = np.sum(a)  # 15

# Cumulative sum
cumsum = np.cumsum(a)  # [1, 3, 6, 10, 15]
```

## Linear Algebra

```python
# Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)  # [[19, 22], [43, 50]]
# Alternative: c = a @ b  # Python 3.5+

# Matrix inverse
a_inv = np.linalg.inv(a)

# Matrix determinant
det = np.linalg.det(a)  # -2.0

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(a)

# Solve linear system Ax = b
b = np.array([1, 2])
x = np.linalg.solve(a, b)  # [-1.0, 1.5]
```

## Indexing and Slicing

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get a specific element
element = a[1, 2]  # 6

# Get a row
row = a[1]  # [4, 5, 6]

# Get a column
col = a[:, 1]  # [2, 5, 8]

# Slicing
slice1 = a[0:2, 1:3]  # [[2, 3], [5, 6]]

# Boolean indexing
mask = a > 5
filtered = a[mask]  # [6, 7, 8, 9]

# Fancy indexing
indices = np.array([0, 2])
selected_rows = a[indices]  # [[1, 2, 3], [7, 8, 9]]
```

## Mathematical Functions

```python
a = np.array([0, np.pi/4, np.pi/2])

# Trigonometric functions
sin_vals = np.sin(a)  # [0.0, 0.7071, 1.0]
cos_vals = np.cos(a)  # [1.0, 0.7071, 0.0]
tan_vals = np.tan(a)  # [0.0, 1.0, inf]

# Exponential and logarithmic functions
exp_vals = np.exp(a)  # [1.0, 2.1932, 4.8105]
log_vals = np.log(np.array([1, 10, 100]))  # [0.0, 2.3026, 4.6052]

# Rounding functions
b = np.array([1.2, 1.5, 1.8, 2.1])
rounded = np.round(b)  # [1.0, 2.0, 2.0, 2.0]
floor = np.floor(b)  # [1.0, 1.0, 1.0, 2.0]
ceil = np.ceil(b)  # [2.0, 2.0, 2.0, 3.0]
```

## Financial Functions

```python
# Net Present Value
cashflows = np.array([-100, 20, 40, 60, 80])
npv = np.npv(0.08, cashflows)  # ~62.65

# Internal Rate of Return
irr = np.irr(cashflows)  # ~0.2094

# Future Value
fv = np.fv(0.08/12, 5*12, -100, -100)  # ~6289.87

# Present Value
pv = np.pv(0.08/12, 5*12, -100, 0)  # ~5197.25
```

## Volatility Calculations (Relevant for Options Trading)

```python
# Calculate daily returns
prices = np.array([100, 102, 99, 101, 103, 102, 105])
daily_returns = np.diff(prices) / prices[:-1]  # [0.02, -0.0294, 0.0202, 0.0198, -0.0097, 0.0294]

# Calculate volatility (standard deviation of returns)
volatility = np.std(daily_returns)  # ~0.0216

# Annualized volatility (assuming 252 trading days)
annualized_volatility = volatility * np.sqrt(252)  # ~0.3427

# Calculate historical volatility using log returns
log_returns = np.log(prices[1:] / prices[:-1])
historical_volatility = np.std(log_returns) * np.sqrt(252)  # ~0.3414
```

## Yang-Zhang Volatility Estimator (Used in Options Strategies)

```python
# Yang-Zhang volatility estimator combines open-high-low-close price data
# This is a simplified implementation
def yang_zhang_volatility(opens, highs, lows, closes, n=20):
    """
    Calculate Yang-Zhang volatility
    
    Parameters:
    opens, highs, lows, closes: numpy arrays of price data
    n: lookback period
    
    Returns:
    Yang-Zhang volatility estimate
    """
    # Overnight volatility
    overnight_returns = np.log(opens[1:] / closes[:-1])
    overnight_vol = np.sum(overnight_returns**2) / (len(overnight_returns) - 1)
    
    # Open-to-Close volatility
    open_close_returns = np.log(closes[1:] / opens[1:])
    open_close_vol = np.sum(open_close_returns**2) / (len(open_close_returns) - 1)
    
    # Rogers-Satchell volatility
    rs_vol = np.zeros(len(highs) - 1)
    for i in range(len(rs_vol)):
        rs_vol[i] = np.log(highs[i+1]/opens[i+1]) * np.log(highs[i+1]/closes[i+1]) + \
                    np.log(lows[i+1]/opens[i+1]) * np.log(lows[i+1]/closes[i+1])
    rs_vol = np.sum(rs_vol) / (len(rs_vol) - 1)
    
    # Combine components with weights
    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    yang_zhang = overnight_vol + k * open_close_vol + (1 - k) * rs_vol
    
    return np.sqrt(yang_zhang)
