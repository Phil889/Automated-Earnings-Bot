# Alpaca Trading API Documentation

This document contains code snippets and examples for using the Alpaca Trading API with the official Python SDK (alpaca-py).

## Setting Up Alpaca API Environment

### Basic Setup

```python
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key', paper=True)
```

### Complete Setup for Options Trading

```python
# Install or upgrade the package `alpaca-py`
!python3 -m pip install --upgrade alpaca-py

import pandas as pd
import numpy as np
from scipy.stats import norm
import alpaca
from scipy.optimize import brentq
from datetime import datetime, time
from zoneinfo import ZoneInfo

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import (
    MarketOrderRequest,
    GetOptionContractsRequest,
    MarketOrderRequest,
    OptionLegRequest,
    ClosePositionRequest,
)
from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.data.historical.stock import StockHistoricalDataClient, StockLatestTradeRequest
from alpaca.data.requests import OptionLatestQuoteRequest
from alpaca.trading.enums import (
    AssetStatus,
    OrderSide,
    OrderClass,
    OrderType,
    TimeInForce,
    ContractType
)
```

### Secure Configuration with Google Colab

```python
# A safe approach to setting up API credentials for Alpaca (Assume you run this notebook in Google Colab)
from google.colab import userdata
API_KEY = userdata.get('ALPACA_API_KEY')
API_SECRET = userdata.get('ALPACA_SECRET_KEY')
BASE_URL = None
PAPER = True # For paper trading environment

# Initialize Alpaca clients
trade_client = TradingClient(api_key=API_KEY, secret_key=API_SECRET, paper=PAPER, url_override=BASE_URL)
option_historical_data_client = OptionHistoricalDataClient(api_key=API_KEY, secret_key=API_SECRET, url_override=BASE_URL)
stock_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=API_SECRET)
```

## Account Information

### Retrieving Account Details

```python
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key')

account = trading_client.get_account()
```

## Orders

### Creating a Market Order

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )
```

### Creating a Limit Order

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )

# Limit order
limit_order = trading_client.submit_order(
                order_data=limit_order_data
              )
```

### Getting Filtered Orders

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# params to filter orders by
request_params = GetOrdersRequest(
                    status=QueryOrderStatus.OPEN,
                    side=OrderSide.SELL
                 )

# orders that satisfy params
orders = trading_client.get_orders(filter=request_params)
```

### Cancelling All Orders

```python
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# attempt to cancel all open orders
cancel_statuses = trading_client.cancel_orders()
```

## Positions

### Getting All Positions

```python
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key')

trading_client.get_all_positions()
```

### Getting a Specific Position

```python
alpaca.trading.client.TradingClient.get_open_position
```

### Closing All Positions

```python
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key')

# closes all position AND also cancels all open orders
trading_client.close_all_positions(cancel_orders=True)
```

### Closing a Specific Position

```python
alpaca.trading.client.TradingClient.close_position
```

### Exercising an Option Contract

```python
alpaca.trading.client.TradingClient.exercise_options_position
```

## Options Trading

### Closing Option Spread Positions

```python
# Exit the spread by liquidating the position
def close_spread(short_symbol, long_symbol):

    # Close the long put by selling it
    trade_client.close_position(
        symbol_or_asset_id = long_symbol,
        close_options = ClosePositionRequest(qty = "1")
    )

    # Close the short put by buying it back
    trade_client.close_position(
        symbol_or_asset_id = short_symbol,
        close_options = ClosePositionRequest(qty = "1")
    )
```

## Market Data

### Retrieving Underlying Stock Price

```python
# Get the latest price of the underlying stock
def get_underlying_price(symbol):
    # Get the latest trade for the underlying stock
    underlying_trade_request = StockLatestTradeRequest(symbol_or_symbols=symbol)
    underlying_trade_response = stock_data_client.get_stock_latest_trade(underlying_trade_request)
    return underlying_trade_response[symbol].price

# Get the latest price of the underlying stock
underlying_price = get_underlying_price(underlying_symbol)
print(f"{underlying_symbol} price: {underlying_price}")
```

### Retrieving Market Calendar

```python
alpaca.trading.client.TradingClient.get_calendar
```

### Getting Assets with Filtering

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

trading_client = TradingClient('api-key', 'secret-key')

# search for crypto assets
search_params = GetAssetsRequest(asset_class=AssetClass.CRYPTO)

assets = trading_client.get_all_assets(search_params)
```

### Retrieving Corporate Actions

```python
alpaca.trading.client.TradingClient.get_corporate_announcements
```

## Streaming Data

### Streaming Trade Updates with Websockets

```python
from alpaca.trading.stream import TradingStream

trading_stream = TradingStream('api-key', 'secret-key', paper=True)

async def update_handler(data):
    # trade updates will arrive in our async handler
    print(data)

# subscribe to trade updates and supply the handler as a parameter
trading_stream.subscribe_trade_updates(update_handler)

# start our websocket streaming
trading_stream.run()
