# Documentation for Automated Earnings Bot

This folder contains documentation for the key libraries and APIs used in the Automated Earnings Bot project.

## Contents

- [Alpaca Trading API Documentation](alpaca_api_docs.md) - Documentation for the Alpaca Markets API, which is used for brokerage functions (account data, order placement, market calendar).
- [Polygon.io API Documentation](polygon_api_docs.md) - Documentation for the Polygon.io API, which is used for market data (stock history, options chain, options quotes/IV, earnings calendar).
- [APScheduler Documentation](apscheduler_docs.md) - Documentation for the APScheduler library, which is used for scheduling tasks.
- [Pandas Documentation](pandas_docs.md) - Documentation for pandas, which is used for data manipulation and time series analysis.
- [NumPy Documentation](numpy_docs.md) - Documentation for NumPy, which is used for numerical operations and array manipulations.
- [SciPy Documentation](scipy_docs.md) - Documentation for SciPy, which is used for interpolation, particularly for building the IV term structure spline.

## Purpose

This documentation has been gathered to provide up-to-date reference material for implementing the core functionality of the Automated Earnings Bot. It includes code snippets and examples that can be directly used or adapted for the project. The documentation focuses on the specific functionality needed for the bot, such as:

- Interacting with brokerage APIs (Alpaca)
- Fetching market data (Polygon.io)
- Scheduling tasks (APScheduler)
- Manipulating time series data (pandas)
- Performing numerical calculations (NumPy)
- Building interpolation splines for IV term structure (SciPy)

## How to Use

When implementing specific components of the bot, refer to the relevant documentation file for guidance on how to use the corresponding API or library. The documentation is organized by topic and includes examples for common use cases.

For example:
- When implementing `alpaca_api.py`, refer to the Alpaca Trading API documentation.
- When implementing `polygon_data.py`, refer to the Polygon.io API documentation.
- When implementing `scheduler.py`, refer to the APScheduler documentation.

## Updating Documentation

If you need to update or add to this documentation, you can use the Context7 MCP server to retrieve the latest information for the relevant libraries.
