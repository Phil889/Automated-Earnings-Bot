# Polygon.io API Documentation

This document contains code snippets and examples for using the Polygon.io API with the official Python client library.

## Basic Usage

### Initializing the Client

```python
from polygon import RESTClient

# Initialize with your API key
client = RESTClient("YOUR_API_KEY")
```

## Market Data

### Fetching Market Data

```python
ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
for trade in trades:
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)
```

### Using Filter Parameters

```python
options_chain = []
for o in client.list_snapshot_options_chain(
    "HCP",
    params={
        "expiration_date.gte": "2024-03-16",
        "strike_price.gte": 29,
        "strike_price.lte": 30,
    },
):
    options_chain.append(o)

print(options_chain)
print(len(options_chain))
```

## Aggregates (Bars)

### List Aggregates

```python
polygon.RESTClient.list_aggs
```

### Get Aggregates

```python
polygon.RESTClient.get_aggs
```

### Get Grouped Daily Aggregates

```python
polygon.RESTClient.get_grouped_daily_aggs
```

### Get Daily Open/Close Aggregates

```python
polygon.RESTClient.get_daily_open_close_agg
```

### Get Previous Close Aggregates

```python
polygon.RESTClient.get_previous_close_agg
```

## Quotes

### List Quotes

```python
polygon.RESTClient.list_quotes
```

### Get Last Quote

```python
polygon.RESTClient.get_last_quote
```

## Reference Data

### List Tickers

```python
polygon.RESTClient.list_tickers
```

### Get Ticker Details

```python
polygon.RESTClient.get_ticker_details
```

### List Ticker News

```python
polygon.RESTClient.list_ticker_news
```

### Get Ticker Types

```python
polygon.RESTClient.get_ticker_types
```

### List Splits

```python
polygon.RESTClient.list_splits
```

### List Dividends

```python
polygon.RESTClient.list_dividends
```

### List Conditions

```python
polygon.RESTClient.list_conditions
```

### Get Exchanges

```python
polygon.RESTClient.get_exchanges
```

## Options Data

### Options Contracts

```
# Get option contract
polygon.RESTClient.get_options_contract

# List Options Contracts
polygon.RESTClient.list_options_contracts
```

## Market Status

### Get Market Status

```python
polygon.RESTClient.get_market_status
```

### Get Market Holidays

```python
polygon.RESTClient.get_market_holidays
```

## Advanced Features

### Accessing vX Methods

```python
financials = RESTClient().vx.list_stock_financials()
```

## Models

The Polygon.io Python client includes various models for handling different types of financial data:

```python
polygon.rest.models.UniversalSnapshot
polygon.rest.models.UniversalSnapshotSession
polygon.rest.models.UniversalSnapshotLastQuote
polygon.rest.models.UniversalSnapshotLastTrade
polygon.rest.models.UniversalSnapshotDetails
polygon.rest.models.UniversalSnapshotUnderlyingAsset
polygon.rest.models.Agg
polygon.rest.models.GroupedDailyAgg
polygon.rest.models.DailyOpenCloseAgg
polygon.rest.models.PreviousCloseAgg
polygon.rest.models.Trade
polygon.rest.models.LastTrade
polygon.rest.models.CryptoTrade
polygon.rest.models.Quote
polygon.rest.models.LastQuote
polygon.rest.models.MinuteSnapshot
polygon.rest.models.TickerSnapshot
polygon.rest.models.DayOptionContractSnapshot
polygon.rest.models.OptionDetails
polygon.rest.models.Greeks
polygon.rest.models.UnderlyingAsset
polygon.rest.models.OptionContractSnapshot
polygon.rest.models.OrderBookQuote
polygon.rest.models.SnapshotTickerFullBook
polygon.rest.models.Ticker
polygon.rest.models.CompanyAddress
polygon.rest.models.Branding
polygon.rest.models.Publisher
polygon.rest.models.TickerDetails
polygon.rest.models.TickerNews
polygon.rest.models.TickerTypes
polygon.rest.models.MarketHoliday
polygon.rest.models.MarketCurrencies
polygon.rest.models.MarketExchanges
polygon.rest.models.MarketStatus
polygon.rest.models.Split
polygon.rest.models.Dividend
polygon.rest.models.SipMapping
polygon.rest.models.Consolidated
polygon.rest.models.MarketCenter
polygon.rest.models.UpdateRules
polygon.rest.models.Condition
polygon.rest.models.Exchange
```

## Enums

The client provides several enums for use with the API:

```python
polygon.rest.models.AssetClass
polygon.rest.models.DataType
polygon.rest.models.SIP
polygon.rest.models.Direction
polygon.rest.models.SnapshotMarketType
