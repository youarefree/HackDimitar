import unittest
from airlines import Flight
from airlines import Date

class test_airline_methods(unittest.TestCase):

    def setUp(self):
        self.flight = Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'), passengers=100, max_passengers=120, from_dest="Sofia", to_dest="London", terminal=Terminal(2, 30), declined=False)

    def
