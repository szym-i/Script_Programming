from enum import Enum, unique

@unique
class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6
    def difference(self,day):
        return day.value - self.value

days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Nidziela"]

class Term:
    def __init__(self, term_day, term_hour, term_minute, term_duration):
        self.day = term_day
        self.hour = term_hour
        self.minute = term_minute
        self.end_hour = (term_hour + (term_duration + term_minute)//60)%24
        self.end_minute = (term_minute + term_duration%60)%60
        self.duration = term_duration

    def __str__(self):
        if self.minute < 10:
            return f'{days[self.day.value]} {self.hour}:0{str(self.minute)} [{self.duration}]'
        return f'({days[self.day.value]} {self.hour}:{self.minute}-{self.end_hour}:{self.end_minute})'

    def earlierThan(self, term):
        end_hour = (self.hour + (self.duration+self.minute)//60)%24
        end_minute = (self.minute + self.duration%60)%60
        if self.__day.value < term.__day.value:
            return True
        if self.__day.value == term.__day.value:
            if end_hour < term.hour: 
                return True
            elif end_hour == term.hour:
                if end_minute < term.minute:
                    return True
        return False
    
    def laterThan(self, term):
        end_hour = (term.hour + (term.minute+term.duration)//60)%24
        end_minute = (term.minute + term.duration%60)%60
        if self.day.value > term.day.value:
            return True
        if self.day.value == term.day.value:
            if self.hour > end_hour:
                return True
            elif self.hour == end_hour:
                if self.minute > end_minute:
                    return True
        return False

    def equals(self, term):
        if self.day.value == term.day.value and self.hour == term.hour and self.minute == term.minute and self.duration == term.duration:
            return f'Terms {self} and {term} are equal'
        else:
            return f'Terms {self} and {term} are NOT equal'

years = ["0","Pierwszy","Drugi","Trzeci","Czwarty"]
full_time = ["zaocznych","stacjonarnych"]

class Lesson:
    def __init__(self, lesson_term, lesson_name, lesson_lecturer, lesson_year):
        self.term = lesson_term
        self.name = lesson_name
        self.lecturer = lesson_lecturer
        self.year = lesson_year
        self.full_time = True

    def __str__(self):
        return f'{self.name} {self.term}\n{years[self.year]} rok studiów {full_time[self.full_time]}\nProwadzący: {self.lecturer}'


if __name__ == '__main__':
    lesson = Lesson(Term(Day.MON,10,50,60),"Programowanie Skryptowe","Stanisław Polak",2)
    print(lesson)
    #term2 = Term(Day.TUE,9,50,60)
    #term3 = Term(Day.TUE,9,50,60)
    #print(term1.__str__())
    #print(term2.__str__())
    #print(term2.earlierThan(term1))
    #print(term2.laterThan(term1))
    #print(term2.equals(term3))

