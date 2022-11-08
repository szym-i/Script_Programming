from DeanerySystem.day import Day
days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Nidziela"]

class Term:
    def __init__(self, day, hour, minute, duration = 90):
        self.__day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        if self.minute < 10:
            return f'{days[self.__day.value]} {self.hour}:0{str(self.minute)} [{self.duration}]'
        return f'{days[self.__day.value]} {self.hour}:{self.minute} [{self.duration}]'

    def __eq__(self,other):
        if self.equals(other):
            return True
        return False
    
    def __gt__(self,other):
        if self.laterThan(other):    
            return True
        return False

    def __ge__(self,other):
        if self.laterThan(other) or self.equals(other):
            return True
        return False

    def __lt__(self,other):
        if self.earlierThan(other):
            return True
        return False

    def __le__(self,other):
        if self.earlierThan(other) or self.equals(other):
            return True
        return False

    def __sub__(self,other):
        end_hour = (other.hour + (other.duration+other.minute)//60)%24
        end_minute = (other.minute + other.duration%60)%60
        duration = 1440*abs(self.__day.value-other.__day.value)+(end_hour - other.hour)*60+end_minute+self.minute 
        return Term(other.__day,other.hour,other.minute,duration) 

    def earlierThan(self, term):
        if self.__day.value < term.__day.value:
            return True
        if self.__day.value == term.__day.value:
            if self.hour < term.hour: 
                return True
            elif self.hour == term.hour:
                if self.minute < term.minute:
                    return True
        return False
    
    def laterThan(self, term):
        if self.__day.value > term.__day.value:
            return True
        if self.__day.value == term.__day.value:
            if self.hour > term.hour:
                return True
            elif self.hour == term.hour:
                if self.minute > term.minute:
                    return True
        return False

    def equals(self, term):
        if self.__day.value == term.__day.value and self.hour == term.hour and self.minute == term.minute and self.duration == term.duration:
            return True
        return False
