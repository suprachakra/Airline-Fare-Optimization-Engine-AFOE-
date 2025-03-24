"""
test_schedule_importer.py
Tests for ScheduleImporter module.
Verifies that new flight schedules are correctly imported and processed.
"""

import unittest
from src.ScheduleImporter import import_schedule, process_schedule

class TestScheduleImporter(unittest.TestCase):
    def test_process_schedule(self):
        raw_data = [
            {"flight_number": "NP123", "status": "new", "departure": "2023-07-01T08:00:00Z"},
            {"flight_number": "NP456", "status": "cancelled", "departure": "2023-07-01T09:00:00Z"}
        ]
        processed = process_schedule(raw_data)
        self.assertEqual(len(processed), 1)
        self.assertEqual(processed[0]["flight_number"], "NP123")

if __name__ == '__main__':
    unittest.main()
