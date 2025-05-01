# Logging setup for the Automated Earnings Calendar Straddle Bot
import logging
import config
import os # For potential log file handler

def setup_logger():
    """Sets up the root logger for the application."""
    log_level = getattr(logging, config.LOG_LEVEL.upper(), logging.INFO)

    # Configure root logger
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        # handlers=[logging.StreamHandler(sys.stdout)] # Default handler is StreamHandler to stderr
                       )

    # Optional: Add a file handler
    # log_file = "bot.log"
    # file_handler = logging.FileHandler(log_file)
    # file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    # logging.getLogger().addHandler(file_handler)


    # Prevent urllib3/requests/asyncio from logging too much noise
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("polygon").setLevel(logging.INFO) # Polygon client can be chatty, adjust as needed
    logging.getLogger("alpaca_trade_api").setLevel(logging.INFO) # Alpaca client chatty too

    # Get the root logger
    root_logger = logging.getLogger()
    # Ensure timezone is handled correctly in logs (APScheduler often helps here, but explicit formatter can too)
    # Example formatter with timezone:
    # formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(name)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # for handler in root_logger.handlers:
    #    handler.setFormatter(formatter)
