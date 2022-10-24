class Term:
    def __init__(self, term_hour, term_minute, term_duration):
        self.hour = term_hour
        self.minute = term_minute
        self.duration = term_duration

    def __str__(self):
        if self.minute < 10:
            return f'{self.hour}:0{str(self.minute)} [{self.duration}]'
        return f'{self.hour}:{self.minute} [{self.duration}]'

    def earlierThan(self, term):
        end_hour = (self.hour + (self.duration+self.minute)//60)%24
        end_minute = (self.minute + self.duration%60)%60
        if end_hour < term.hour: 
            return True
        elif end_hour == term.hour:
            if end_minute < term.minute:
                return True
        return False
    
    def laterThan(self, term):
        end_hour = (term.hour + (term.minute+term.duration)//60)%24
        end_minute = (term.minute + term.duration%60)%60
        if self.hour > end_hour:
            return True
        elif self.hour == end_hour:
            if self.minute > end_minute:
                return True
        return False

    def equals(self, term):
        if self.hour == term.hour and self.minute == term.minute and self.duration == term.duration:
            return True
        return False

if __name__ == '__main__':
    term1 = Term(10,50,60)
    term2 = Term(9,50,60)
    print(term1.__str__())
    print(term2.__str__())
    print(term1.earlierThan(term2))
    print(term1.laterThan(term2))
    print(term1.equals(term1))
    
