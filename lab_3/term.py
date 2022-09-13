class Term:
    def __init__(self, term_hour, term_minute, term_duration):
        self.hour = term_hour
        self.minute = term_minute
        self.duration = term_duration

    def __str__(self):
        return f'{self.hour}:{self.minute} [{self.duration}]'

if __name__ == '__main__':
    term = Term(10,11,90)
    print(term.__str__())
