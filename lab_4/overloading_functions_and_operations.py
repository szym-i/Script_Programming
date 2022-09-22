class Term:
    def __init__(self, term_hour, term_minute, term_duration):
        self.hour = term_hour
        self.minute = term_minute
        self.duration = term_duration

    def __str__(self):
        if self.minute < 10:
            return f'{self.hour}:0{str(self.minute)} [{self.duration}]'
        return f'{self.hour}:{self.minute} [{self.duration}]'
    
    def __eq__(self,other):
        if self.equals(other):
            return True
        return False
    
    def __gt__(self,other):
        if self.hour > other.hour:
            return True
        if self.hour == other.hour:
            if self.minute > other.minute:
                return True
        return False

    def __ge__(self,other):
        if self.hour > other.hour:
            return True
        if self.hour == other.hour:
            if self.minute >= other.minute:
                return True
        return False

    def __lt__(self,other):
        if self.hour < other.hour:
            return True
        if self.hour == other.hour:
            if self.minute < other.minute:
                return True
        return False

    def __le__(self,other):
        if self.hour < other.hour:
            return True
        if self.hour == other.hour:
            if self.minute <= other.minute:
                return True
        return False

    def __sub__(self,other):
        return Term(self.hour,self.minute,1)

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
        else:
            return False

if __name__ == '__main__':
    term1 = Term(8,30,90)
    term2 = Term(9,45,30)
    term3 = Term(9,45,90)
    print(term1)
    print(term2)
    print(term3)
    print("term1 < term2",term1 < term2)
    print("term1 <=term2",term1 <=term2)
    print("term1 > term2",term1 > term2)
    print("term1 >= term2", term1 >= term2)
    print("term2 == term2:",term2 == term2)
    print("term2 == term3:",term2 == term3)
    term4 = term3 - term1
    print(term4)
