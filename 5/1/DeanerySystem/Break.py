from term import Term

class Break:
    def __init__(self,term: Term):
        self.duration = 10
        self.hour = term.end_hour
        self.minute = term.end_minute

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        return f"Przerwa {self.hour}:{self.minute}-{self.hour+(self.minute+self.duration)//60}:{(self.minute+self.duration)%60}"

