"""
Config.py
Utility for loading configuration settings from YAML files, environment variables,
or a secret manager. This module centralizes configuration for cross-cutting concerns.
"""

import os
import yaml

def load_config(config_path="config.yaml"):
    """
    Loads configuration from a YAML file.
    Returns the configuration as a dictionary.
    """
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        raise Exception("Failed to load configuration: " + str(e))

def get_env_or_config(key, default=None, config=None):
    """
    Retrieves a configuration value from environment variables or a provided config dictionary.
    """
    return os.getenv(key, config.get(key, default) if config else default)

# Example usage:
# config = load_config("config.yaml")
# db_host = get_env_or_config("DB_HOST", "localhost", config)
