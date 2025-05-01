# Automated Earnings Calendar Straddle Bot

An automated trading bot that implements a Calendar Straddle options strategy based on upcoming corporate earnings announcements.

## Project Overview

This bot automates the process of:
1. Identifying stocks with earnings reports scheduled for the next trading day
2. Filtering potential trades based on predefined criteria (volume, IV/RV ratio, term structure slope)
3. Calculating appropriate position sizing based on portfolio value
4. Entering trades (buy back-month ATM straddle, sell front-month ATM straddle) shortly before market close
5. Exiting trades shortly after market open on the day of earnings

## Project Structure

```
automated_earnings_bot/
├── config.py               # Configuration variables
├── logger.py               # Centralized logging setup
├── alpaca_api.py           # Interface for Alpaca Brokerage API
├── polygon_data.py         # Interface for Polygon.io Data API
├── strategy_calculator.py  # Strategy filtering and calculation logic
├── order_builder.py        # Constructs brokerage-specific order definitions
├── portfolio_tracker.py    # Manages portfolio state and trade history
├── scheduler.py            # Main entry point, schedules and runs jobs
├── portfolio_data.json     # State persistence file
└── docs/                   # Documentation for libraries and APIs
    ├── README.md           # Documentation overview
    ├── alpaca_api_docs.md  # Alpaca API documentation
    ├── polygon_api_docs.md # Polygon.io API documentation
    ├── apscheduler_docs.md # APScheduler documentation
    ├── pandas_docs.md      # pandas documentation
    ├── numpy_docs.md       # NumPy documentation
    └── scipy_docs.md       # SciPy documentation
```

## Requirements

- Python 3.8+
- Alpaca Markets account (Paper Trading initially)
- Polygon.io account with a paid plan (for options data)
- Required Python packages:
  ```
  pandas
  numpy
  scipy
  alpaca-trade-api
  polygon-api-client
  APScheduler
  pytz
  ```

## Setup

1. Clone the repository
2. Install required packages:
   ```
   pip install pandas numpy scipy alpaca-trade-api polygon-api-client APScheduler pytz
   ```
3. Configure API keys:
   - Set environment variables for security:
     ```
     export ALPACA_API_KEY="your_alpaca_api_key"
     export ALPACA_SECRET_KEY="your_alpaca_secret_key"
     export POLYGON_API_KEY="your_polygon_api_key"
     ```
   - Or update `config.py` directly (not recommended for production)
4. Adjust strategy parameters in `config.py` if desired
5. Run the bot:
   ```
   python scheduler.py
   ```

## Strategy Details

The bot implements a Calendar Straddle strategy around earnings announcements:
- Buy ATM straddle in back-month expiration
- Sell ATM straddle in front-month expiration
- Enter before market close on the day before earnings
- Exit after market open on the day of earnings

Filtering criteria:
- Volume threshold: Minimum average daily volume
- IV/RV ratio threshold: Implied volatility relative to realized volatility
- Term structure slope threshold: Slope of the IV term structure

## Documentation

The `docs/` directory contains comprehensive documentation for all the key libraries and APIs used in this project. This documentation has been gathered to provide up-to-date reference material for implementing the core functionality of the bot. It includes code snippets and examples that can be directly used or adapted for the project.

The documentation covers:
- Alpaca Trading API for brokerage functions
- Polygon.io API for market data
- APScheduler for task scheduling
- pandas for data manipulation and time series analysis
- NumPy for numerical operations
- SciPy for interpolation (particularly for IV term structure)

Refer to the [docs/README.md](docs/README.md) file for more information.

## Development Status

This project is currently in development. See the implementation checklist in the original detailed plan.

## Disclaimer

This bot is for educational and research purposes only. Trading options involves significant risk. Use at your own risk and only with paper trading until thoroughly tested.
