from day import Day
import math

days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]

class Term:
    def __init__(self, term_day, term_hour, term_minute, term_duration = 90):
        self.day = term_day
        self.hour = term_hour
        self.minute = term_minute
        self.end_hour = (term_hour + (term_duration + term_minute)//60)%24
        self.end_minute = (term_minute + term_duration%60)%60
        self.duration = term_duration

    def __str__(self):
        if self.minute < 10 and self.end_minute < 10:
            return f'({days[self.day.value]} {self.hour}:0{str(self.minute)}-{self.end_hour}:0{self.end_minute})'
        if self.minute < 10:
            return f'({days[self.day.value]} {self.hour}:0{str(self.minute)}-{self.end_hour}:{self.end_minute})'
        if self.end_minute < 10:
            return f'({days[self.day.value]} {self.hour}:{str(self.minute)}-{self.end_hour}:0{self.end_minute})'
        return f'({days[self.day.value]} {self.hour}:{self.minute}-{self.end_hour}:{self.end_minute})'
    
    def earlierThan(self, term):
        if self.day.value < term.day.value:
            return True
        if self.day.value == term.day.value:
            if self.hour < term.hour: 
                return True
            elif self.hour == term.hour:
                if self.minute < term.minute:
                    return True
        return False
    
    def laterThan(self, term):
        if self.day.value > term.day.value:
            return True
        if self.day.value == term.day.value:
            if self.hour > term.hour:
                return True
            elif self.hour == term.hour:
                if self.minute > term.minute:
                    return True
        return False

    def equals(self, term):
        if self.day.value == term.day.value and self.hour == term.hour and self.minute == term.minute and self.duration == term.duration:
            return True
        else:
            return False

    def is_full_time(self):
        if self.day.value >= 5:
            return False
        if self.day.value == 4:
            if self.end_hour > 17:
                return False
            if self.end_hour == 17:
                if self.end_minute != 0:
                    return False
        return True

    def is_valid(self):
        if self.end_hour > 20:
            return False
        if self.end_hour == 20:
            if self.end_minute != 0:
                return False
        if self.hour < 8:
            return False
        return True
