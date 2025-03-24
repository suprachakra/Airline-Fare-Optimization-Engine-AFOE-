"""
CurrencyConverter.py
Utility to convert fares between currencies.
Uses a simplified exchange rate lookup (in production, integrate with a currency API).
"""

def convert(amount, from_currency, to_currency):
    # For demonstration, we use a static conversion rate.
    # In production, you might query an external API.
    exchange_rates = {
        "USD": {"EUR": 0.9, "GBP": 0.8},
        "EUR": {"USD": 1.11, "GBP": 0.88},
        "GBP": {"USD": 1.25, "EUR": 1.14}
    }
    
    if from_currency == to_currency:
        return amount
    try:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    except KeyError:
        raise ValueError("Unsupported currency conversion: {} to {}".format(from_currency, to_currency))

# Example usage:
# converted_amount = convert(100, "USD", "EUR")
