days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Nidziela"]


class Term:
    def __init__(self,term_day, term_hour, term_minute):
        self.__day = term_day
        self.hour = term_hour
        self.minute = term_minute
        self.duration = 90

    def __str__(self):
        if self.minute < 10:
            return f'{days[self.__day.value]} {self.hour}:0{str(self.minute)} [{self.duration}]'
        return f'{days[self.__day.value]} {self.hour}:{self.minute} [{self.duration}]'

    def earlierThan(self, term):
        #end_hour = (self.hour + (self.duration+self.minute)//60)%24
        #end_minute = (self.minute + self.duration%60)%60
        #if self.__day.value < term.__day.value:
       #     return True
        #if self.__day.value == term.__day.value:
         #   if end_hour < term.hour: 
          #      return True
           # elif end_hour == term.hour:
            #    if end_minute < term.minute:
             #       return True
        #return False
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
        #end_hour = (term.hour + (term.minute+term.duration)//60)%24
        #end_minute = (term.minute + term.duration%60)%60
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

if __name__ == '__main__':
    from day import Day
    term1 = Term(Day.MON,10,50)
    term2 = Term(Day.TUE,9,50)
    term3 = Term(Day.TUE,9,50)
    print(term1.__str__())
    print(term2.__str__())
    print(term2.earlierThan(term1))
    print(term2.laterThan(term1))
    print(term2.equals(term3))
    
