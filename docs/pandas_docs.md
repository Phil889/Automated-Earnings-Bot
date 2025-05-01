# Pandas Documentation: Time Series Data

This document contains code snippets and examples for using pandas for time series data manipulation, which is relevant for the Automated Earnings Bot project.

## Creating Time Series Data

### Creating a DatetimeIndex

```python
# Create a DatetimeIndex with daily frequency
dates = pd.date_range('1/1/2000', periods=8)

# Create a DataFrame with a DatetimeIndex
df = pd.DataFrame(np.random.randn(8, 4),
                 index=dates, columns=['A', 'B', 'C', 'D'])
```

### Creating a Time Series with Random Data

```python
# Create a time series with secondly frequency
rng = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

# Create a sparse time series (daily with 1 second offset)
rng = pd.date_range("2014-1-1", periods=100, freq="D") + pd.Timedelta("1s")
ts = pd.Series(range(100), index=rng)
```

## Time Series Operations

### Resampling

```python
# Downsample to 5-minute frequency and sum values
ts.resample("5Min").sum()

# Downsample to business day frequency and get the last value
s.resample("B").last()

# Downsample with right label and closed parameters
s.resample("B", label="right", closed="right").last()

# Upsample from secondly to 250-millisecond frequency
# Fill gaps with NaN
ts[:2].resample("250ms").asfreq()

# Forward fill gaps
ts[:2].resample("250ms").ffill()

# Forward fill with limit
ts[:2].resample("250ms").ffill(limit=2)
```

### Efficient Resampling for Sparse Time Series

```python
from functools import partial
from pandas.tseries.frequencies import to_offset

def round(t, freq):
    # round a Timestamp to a specified freq
    freq = to_offset(freq)
    td = pd.Timedelta(freq)
    return pd.Timestamp((t.value // td.value) * td.value)

# Efficiently resample sparse time series
ts.groupby(partial(round, freq="3min")).sum()
```

### Timezone Handling

```python
# Localize a time series to UTC
ts_utc = ts.tz_localize("UTC")

# Convert from UTC to US/Eastern
ts_utc.tz_convert("US/Eastern")

# Arithmetic operations on time zone aware series
ts_utc = pd.Series(range(3), pd.date_range("20130101", periods=3, tz="UTC"))
eastern = ts_utc.tz_convert("US/Eastern")
berlin = ts_utc.tz_convert("Europe/Berlin")
result = eastern + berlin  # Result has UTC index
```

### Date Offsets

```python
# Add business days to a DatetimeIndex
rng + pd.offsets.BusinessDay(5)
```

## Selecting and Filtering Time Series Data

### Selecting by Date String

```python
# Select all data for a specific year
ts['2001']
df['2001']  # For DataFrame

# Select data for a specific day
s[s.dt.day == 2]
```

### Accessing Datetime Properties

```python
# Extract datetime components
s = pd.Series(pd.date_range("20130101 09:10:12", periods=4))
s.dt.hour
s.dt.second
s.dt.day
```

## Visualization

### Basic Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123456)
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
```

### Plotting Daily Mean Values

```python
# Resample to daily frequency and plot mean values
no_2.resample("D").mean().plot(style="-o", figsize=(10, 5))
```

### Lag Plot for Time Series Analysis

```python
from pandas.plotting import lag_plot

plt.figure()
spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))
lag_plot(data)
```

### Autocorrelation Plot

```python
from pandas.plotting import autocorrelation_plot

plt.figure()
spacing = np.linspace(-9 * np.pi, 9 * np.pi, num=1000)
data = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(spacing))
autocorrelation_plot(data)
```

### Plotting with Secondary Y-Axis

```python
# Plot two time series with different y-axes
fx["FR"].plot(style="g")
fx["IT"].plot(style="k--", secondary_y=True)
```

## Advanced Time Series Operations

### Pivot Table with Time-Based Grouping

```python
# Group by month end frequency
pd.pivot_table(df, values="D", index=pd.Grouper(freq="ME", key="F"), columns="C")
```

### Working with Timedeltas

```python
# Create a Series of timedeltas
deltas = pd.Series([datetime.timedelta(days=i) for i in range(3)])

# Calculate time differences
y = s - s.shift()
```

### Converting to NumPy Arrays

```python
# Convert time-zone naive Series to NumPy array
s_naive.to_numpy()  # Results in datetime64[ns] array

# Convert time-zone aware Series to NumPy array
s_aware.to_numpy()  # Results in object array of Timestamps
```

### Creating and Saving Large Time Series Datasets

```python
import pandas as pd
import numpy as np

def make_timeseries(start="2000-01-01", end="2000-12-31", freq="1D", seed=None):
    index = pd.date_range(start=start, end=end, freq=freq, name="timestamp")
    n = len(index)
    state = np.random.RandomState(seed)
    columns = {
        "name": state.choice(["Alice", "Bob", "Charlie"], size=n),
        "id": state.poisson(1000, size=n),
        "x": state.rand(n) * 2 - 1,
        "y": state.rand(n) * 2 - 1,
    }
    df = pd.DataFrame(columns, index=index, columns=sorted(columns))
    if df.index[-1] == end:
        df = df.iloc[:-1]
    return df

# Create multiple time series and concatenate them
timeseries = [
    make_timeseries(freq="1min", seed=i).rename(columns=lambda x: f"{x}_{i}")
    for i in range(10)
]
ts_wide = pd.concat(timeseries, axis=1)

# Save to Parquet file
ts_wide.to_parquet("timeseries_wide.parquet")
