from collections import OrderedDict
from itertools import groupby
from operator import itemgetter

class Restaurant():

    WEEKDAYS = [
        'Sun',
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
    ]

    def __init__(self, *opening_hours):

        # group day with the opening hours
        # [('Mon', '9-17'), ('Tue', '10-15'), ...]
        self.opening_hours = zip(
            self.WEEKDAYS,
            [opening_hour.to_string() for opening_hour in opening_hours]
        )

    def get_opening_hours(self):
        oh = self.opening_hours   
        result_group =[(list(zip(*g)[0]),k) for k, g in groupby(oh,itemgetter(1))]
        result_append = dict(( k[0]+"-"+k[-1] if len(k)>2 else k[0],g)for k,g in result_group)
        d = {}
        for k,v in result_append.iteritems():
            d.setdefault(v,[]).append(k)
        return ', '.join("{}: {}".format(','.join(v), k) for k, v in d.iteritems())
        
        

class OpeningHour():

    def __init__(self, opening_hour, closing_hour):
        self.opening_hour = opening_hour
        self.closing_hour = closing_hour

    def to_string(self):
        return "{}-{}".format(self.opening_hour, self.closing_hour)


# Sun: 8-16, Mon: 8-17, Tue: 8-18, Wed: 8-19, Thu: 8-20, Fri: 8-21, Sat: 8-22
restaurant = Restaurant(
    OpeningHour(8, 16),  # Sunday
    OpeningHour(8, 17),  # Monday
    OpeningHour(8, 18),  # Tuesday
    OpeningHour(8, 19),  # Wednesday
    OpeningHour(8, 20),  # Thursday
    OpeningHour(8, 21),  # Friday
    OpeningHour(8, 22),  # Saturday
)

print(restaurant.get_opening_hours())

# Sun, Thu - Sat: 8-16, Mon - Wed: 8-17
restaurant = Restaurant(
    OpeningHour(8, 16),  # Sunday
    OpeningHour(8, 17),  # Monday
    OpeningHour(8, 17),  # Tuesday
    OpeningHour(8, 17),  # Wednesday
    OpeningHour(8, 16),  # Thursday
    OpeningHour(8, 16),  # Friday
    OpeningHour(8, 16),  # Saturday
)

print(restaurant.get_opening_hours())

# Sun - Wed: 8-16, Thu: 8-20, Fri: 8-21, Sat: 8-22
restaurant = Restaurant(
    OpeningHour(8, 16),  # Sunday
    OpeningHour(8, 16),  # Monday
    OpeningHour(8, 16),  # Tuesday
    OpeningHour(8, 16),  # Wednesday
    OpeningHour(8, 20),  # Thursday
    OpeningHour(8, 21),  # Friday
    OpeningHour(8, 22),  # Saturday
)

print(restaurant.get_opening_hours())
