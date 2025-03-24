"""
Flight.py
Shared Flight Data Model

This model represents flight details such as flight number, route, and schedule.
It is used consistently across services (e.g., Pricing, Forecasting) to ensure data integrity.
"""

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number  # e.g., "AA123"
        self.origin = origin  # e.g., "JFK"
        self.destination = destination  # e.g., "LAX"
        self.departure_time = departure_time  # ISO datetime string (e.g., "2023-06-01T08:00:00Z")
        self.arrival_time = arrival_time  # ISO datetime string

    def to_dict(self):
        return {
            "flight_number": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time
        }

# Example usage:
# flight = Flight("AA123", "JFK", "LAX", "2023-06-01T08:00:00Z", "2023-06-01T11:00:00Z")
# print(flight.to_dict())
