from enum import Enum, unique
import math

@unique
class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

days = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]

class Term:
    def __init__(self, term_day, term_hour, term_minute, term_duration):
        self.day = term_day
        self.hour = term_hour
        self.minute = term_minute
        self.end_hour = (term_hour + (term_duration + term_minute)//60)%24
        self.end_minute = (term_minute + term_duration%60)%60
        self.duration = term_duration

    def __str__(self):
        if self.minute < 10 and self.end_minute < 10:
            return f'({days[self.day.value]} {self.hour}:0{str(self.minute)}-{self.end_hour}:0{self.end_minute})'
        if self.minute < 10:
            return f'({days[self.day.value]} {self.hour}:0{str(self.minute)}-{self.end_hour}:{self.end_minute})'
        if self.end_minute < 10:
            return f'({days[self.day.value]} {self.hour}:{str(self.minute)}-{self.end_hour}:0{self.end_minute})'
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

    def is_full_time(self):
        if self.day.value >= 5:
            return False
        if self.day.value == 4:
            if self.end_hour >= 17:
                return False
        return True

    def is_valid(self):
        if self.end_hour > 20:
            return False
        if self.end_hour == 20:
            if self.end_minute != 0:
                return False
        if self.hour < 8:
            return False
        return True

years = ["0","Pierwszy","Drugi","Trzeci","Czwarty"]
full_time = ["zaocznych","stacjonarnych"]

class Lesson:
    def __init__(self, term, lesson_name, teacherName, year):
        self.term = term
        self.name = lesson_name
        self.teacherName = teacherName
        self.year = year
        self.full_time = self.term.is_full_time()

    def __str__(self):
        return f'{self.name} {self.term}\n{years[self.year]} rok studiów {full_time[self.full_time]}\nProwadzący: {self.teacherName}'

    def laterDay(self):
        self.term.day = Day((self.term.day.value+1)%7)
        self.full_time = self.term.is_full_time()
        return True
    
    def earlierDay(self):
        self.term.day = Day((self.term.day.value-1)%7)
        self.full_time = self.term.is_full_time()
        return True

    def laterTime(self):
        start_hour = (self.term.hour + (self.term.duration+self.term.minute)//60)%24
        start_minute = (self.term.minute + self.term.duration%60)%60
        end_hour = (start_hour + (self.term.duration+start_minute)//60)%24
        end_minute = (start_minute + self.term.duration%60)%60
        if Term(self.term.day,start_hour,start_minute,self.term.duration).is_valid():
            self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            return True
        return False

    def earlierTime(self):
        start_hour = self.term.hour - math.ceil((self.term.duration - self.term.minute)/60)
        start_minute = (self.term.minute-self.term.duration)%60
        if Term(self.term.day, start_hour, start_minute, self.term.duration).is_valid():
            self.term = Term(self.term.day, start_hour, start_minute, self.term.duration)
            return True
        return False

if __name__ == '__main__':
    lesson = Lesson(Term(Day.FRI,18,29,91),"Programowanie Skryptowe","Stanisław Polak",2)
    print(lesson)
    for i in range(0,7):
        lesson.laterDay()
        print(lesson)
    while lesson.laterTime():
        print(lesson)
    while lesson.earlierTime():
        print(lesson)
    print(lesson)
