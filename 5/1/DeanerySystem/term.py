from day import Day
import math

days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]

class Term:
    def __init__(self, day, hour, minute, duration = 90):
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__end_hour = (hour + (duration + minute)//60)%24
        self.__end_minute = (minute + duration%60)%60
        self.__duration = duration

    @property
    def day(self):
        return self.__day

    @property
    def day_value(self):
        return self.__day.value

    @day.setter
    def day(self,var):
        self.__day = var

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self,var):
        self.__hour = var

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self,var):
        self.__minute = var

    @property
    def end_hour(self):
        return self.__end_hour

    @property
    def end_minute(self):
        return self.__end_minute
    
    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        if self.minute < 10 and self.end_minute < 10:
            return f'{days[self.__day.value]} {self.hour}:0{str(self.minute)}-{self.end_hour}:0{self.end_minute}'
        if self.minute < 10:
            return f'{days[self.__day.value]} {self.hour}:0{str(self.minute)}-{self.end_hour}:{self.end_minute}'
        if self.end_minute < 10:
            return f'{days[self.__day.value]} {self.hour}:{str(self.minute)}-{self.end_hour}:0{self.end_minute}'
        return f'{days[self.__day.value]} {self.hour}:{self.minute}-{self.end_hour}:{self.end_minute}'
    
    def earlierThan(self, term) -> bool:
        if self.__day.value < term.__day.value:
            return True
        if self.__day.value == term.__day.value:
            if self.hour < term.hour: 
                return True
            elif self.hour == term.hour:
                if self.minute < term.minute:
                    return True
        return False
    
    def laterThan(self, term) -> bool:
        if self.__day.value > term.__day.value:
            return True
        if self.__day.value == term.__day.value:
            if self.hour > term.hour:
                return True
            elif self.hour == term.hour:
                if self.minute > term.minute:
                    return True
        return False

    def equals(self, term) -> bool:
        if self.__day.value == term.__day.value and self.hour == term.hour and self.minute == term.minute and self.duration == term.duration:
            return True
        else:
            return False

    def is_full_time(self) -> bool:
        if self.__day.value >= 5:
            return False
        if self.__day.value == 4:
            if self.end_hour > 17:
                return False
            if self.end_hour == 17:
                if self.end_minute != 0:
                    return False
        return True

    def is_valid(self) -> bool:
        if self.end_hour > 20:
            return False
        if self.end_hour == 20:
            if self.end_minute != 0:
                return False
        if self.hour < 8:
            return False
        return True
