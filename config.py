# Configuration file for the Automated Earnings Calendar Straddle Bot
import os

# Alpaca API Credentials (USE ENVIRONMENT VARIABLES FOR LIVE TRADING!)
ALPACA_API_KEY = os.environ.get("ALPACA_API_KEY", "YOUR_PAPER_API_KEY")
ALPACA_SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY", "YOUR_PAPER_SECRET_KEY")
ALPACA_BASE_URL = "https://paper-api.alpaca.markets" # Use "https://api.alpaca.markets" for live trading

# --- Polygon.io API Credentials (REQUIRES PAID PLAN) ---
# Ref: https://polygon.io/docs/stocks/getting-started
POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY", "YOUR_POLYGON_PAID_API_KEY")

# --- Strategy Parameters (from YouTube transcript & your code) ---
VOLUME_THRESHOLD = 1500000
IV_RV_RATIO_THRESHOLD = 1.25
TS_SLOPE_THRESHOLD = -0.00406
POSITION_SIZE_PERCENTAGE = 0.06 # 6% of portfolio value max debit
ENTRY_LIMIT_PRICE_BUFFER = 1.05 # Set limit price 5% higher than calculated mid-price debit

# --- Timing ---
# Ref: https://alpaca.markets/docs/api-references/trading-api/account/calendar/ (Times are in EST/EDT)
MARKET_TIMEZONE = 'America/New_York'
ENTRY_MINUTES_BEFORE_CLOSE = 15
EXIT_MINUTES_AFTER_OPEN = 15
DAILY_CHECK_HOUR = 8 # 8:00 AM Market Time for the main daily scheduling job

# --- Other Settings ---
# List of symbols to check (consider using a screener data source for a broader universe)
WATCHLIST_SYMBOLS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'UNH', 'LLY', 'JPM', 'V', 'BRK.B', 'JNJ', 'XOM', 'BAC', 'PG', 'KO'] # Example expanded list
LOG_LEVEL = "INFO" # DEBUG, INFO, WARNING, ERROR

# --- Portfolio Tracker File ---
PORTFOLIO_DATA_FILE = "portfolio_data.json"
STARTING_CAPITAL = 10000.0
