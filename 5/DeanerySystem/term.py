from day import Day
import math

days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]

class BasicTerm:
    def __init__(self,hour,minute,duration=90):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration
    
    def __str__(self):
        return f"{self.hour}:{self.minute} [{self.duration}]"
    
    def __lt__(self,term):
        return self.earlierThan(term)
    
    def __gt__(self,term):
        return self.laterThan(term)
    
    def __le__(self,term):
        return self.earlierThan(term) or self.equals(term)
    
    def __ge__(self,term):
        return self.laterThan(term) or self.equals(term)
    
    def earlierThan(self,term):
        if self.hour < term.hour:
            return True
        elif self.hour == term.hour:
            if self.minute < term.minute:
                return True
        return False
    
    def laterThan(self,term):
        if not self.earlierThan(term) and not self.equals(term):
            return True
        return False
    
    def equals(self,term):
        if self.hour == term.hour and self.minute == term.minute:
            return True
        return False
    
    @property
    def duration(self):
        return self.__duration


    @property
    def end_hour(self):
        end_hour = (self.hour + (self.duration + self.minute)//60)%24
        return end_hour

    @property
    def end_minute(self):
        end_minute = (self.minute + self.duration%60)%60
        return int(end_minute)

    @property
    def hour(self):
        return int(self.__hour)
    
    @hour.setter
    def hour(self,val):
        self.__hour = val

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self,var):
        self.__minute = var


class Term(BasicTerm):

    def __init__(self,day,hour,minute,duration=90):
        super().__init__(hour,minute,duration)
        self.__day = day
    
    def __hash__(self):
        return 60*self.hour + self.minute + 24*60*self.day.value

    @property
    def day(self):
        return self.__day

    @property
    def day_value(self):
        return self.__day.value

    @day.setter
    def day(self,var):
        self.__day = var

    def __repr__(self):
        return str(hash(self))

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


if __name__ == '__main__':
    term1 = Term(Day.MON,8,10)
    d ={}
    for i in range(hash(term1),hash(term1)+term1.duration+1):
        d[i] = term1
    print(d)
