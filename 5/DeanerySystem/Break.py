from term import *

class Break(BasicTerm):
    def __str__(self):
        return "---"

    def getTerm(self):
        if self.minute < 10 and self.end_minute < 10:
            return f'{self.hour}:0{str(self.minute)}-{self.end_hour}:0{self.end_minute}'
        if self.minute < 10:
            return f'{self.hour}:0{str(self.minute)}-{self.end_hour}:{self.end_minute}'
        if self.end_minute < 10:
            return f'{self.hour}:{str(self.minute)}-{self.end_hour}:0{self.end_minute}'
        return f'{self.hour}:{self.minute}-{self.end_hour}:{self.end_minute}'
