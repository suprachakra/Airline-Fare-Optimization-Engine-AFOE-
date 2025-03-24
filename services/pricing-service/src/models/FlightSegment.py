"""
FlightSegment.py
Defines the data model for a flight segment.
Contains details like flight number, route, departure/arrival times, and capacity.
"""

class FlightSegment:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.capacity = capacity

    def to_dict(self):
        return {
            "flight_number": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "capacity": self.capacity
        }

# Example usage:
# segment = FlightSegment("AB123", "JFK", "LAX", "2023-01-01T08:00:00Z", "2023-01-01T11:00:00Z", 150)
