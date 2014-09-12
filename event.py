from datetime import datetime

class Event:
    'Single event to add to the calendar'

    def __init__(
            self, name, place, start, end, weekdays,
            description="", semester=""):
        self.name = name
        self.place = place
        self.description = description
        self.start = start
        self.end = end
        self.weekdays = weekdays
        self.semester = semester