
class Flight:

    def __init__(self, **kwargs):
        self.start_time = kwargs['start_time']



f = Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'), passengers=100, max_passengers=120, from_dest="Sofia", to_dest="London", terminal=Terminal(2, 30), declined=False)




class Date:

    def __init__(self, *args, **kwargs):
        self.day = args[1]
        self.month = args[2]
        self.year = args[3]
        self.hour = kwargs['hour']

