"""
ErrorHandling.py
Common Exception Classes and Error Handling Patterns

Defines custom exceptions and helper functions to format error responses uniformly across services.
"""

class APIError(Exception):
    """
    Custom exception class for API errors.
    """
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.status_code = status_code

def handle_exception(e):
    """
    Formats an exception into a standardized error response.
    Returns a dictionary with error message and status code.
    """
    return {
        "error": str(e),
        "status_code": getattr(e, "status_code", 500)
    }

# Example usage:
# try:
#     # Code that might throw an exception
# except Exception as e:
#     error_response = handle_exception(e)
#     print(error_response)
