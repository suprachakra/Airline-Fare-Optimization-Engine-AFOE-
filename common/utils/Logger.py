"""
Logger.py
Central Logging Utility

This module sets up structured logging and directs logs to appropriate outputs.
It is used by all services to ensure consistent logging and monitoring.
"""

import logging
import sys

def setup_logger(name=__name__, level=logging.INFO):
    """
    Configures and returns a logger with the specified name and logging level.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    handler.setFormatter(formatter)

    # Avoid duplicate handlers if already configured
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

# Example usage:
# logger = setup_logger("common.Logger")
# logger.info("Logger initialized successfully.")
