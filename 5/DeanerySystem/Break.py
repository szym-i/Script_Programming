from term import Term

class Break:
    def __init__(self,term: Term):
        self.term = term

    def __str__(self):
        return "---"

    def getTerm(self):
        if self.term.minute < 10 and self.term.end_minute < 10:
            return f'{self.term.hour}:0{str(self.term.minute)}-{self.term.end_hour}:0{self.term.end_minute}'
        if self.term.minute < 10:
            return f'{self.term.hour}:0{str(self.term.minute)}-{self.term.end_hour}:{self.term.end_minute}'
        if self.term.end_minute < 10:
            return f'{self.term.hour}:{str(self.term.minute)}-{self.term.end_hour}:0{self.term.end_minute}'
        return f'{self.term.hour}:{self.term.minute}-{self.term.end_hour}:{self.term.end_minute}'

if __name__ == '__main__':
    b1 = Break(Term(None,8,30,10))
    print(b1.getTerm())
