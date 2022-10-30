from day import Day
from term import Term
import math

years = ["0","Pierwszy","Drugi","Trzeci","Czwarty"]
full_time = ["zaocznych","stacjonarnych"]

class Lesson:
    def __init__(self, term, lesson_name, teacherName, year):
        self.term = term
        self.name = lesson_name
        self.teacherName = teacherName
        self.year = year
        self.fullTime = self.term.is_full_time()

    def __str__(self):
        return f'{self.name} {self.term}\n{years[self.year]} rok studiów {full_time[self.fullTime]}\nProwadzący: {self.teacherName}'

    def laterDay(self):
        if Term(Day((self.term.day.value+1)%7),self.term.hour,self.term.minute,self.term.duration).is_full_time() != self.fullTime:
            return False
        self.term.day = Day((self.term.day.value+1)%7)
        return True
    
    def earlierDay(self):
        if Term(Day((self.term.day.value-1)%7),self.term.hour,self.term.minute,self.term.duration).is_full_time() != self.fullTime:
            return False
        self.term.day = Day((self.term.day.value-1)%7)
        return True

    def laterTime(self):
        start_hour = (self.term.hour + (self.term.duration+self.term.minute)//60)%24
        start_minute = (self.term.minute + self.term.duration%60)%60
        if Term(self.term.day,start_hour,start_minute,self.term.duration).is_valid()\
        and Term(self.term.day,start_hour,start_minute,self.term.duration).is_full_time() == self.fullTime:
            self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            return True
        return False

    def earlierTime(self):
        start_hour = self.term.hour - math.ceil((self.term.duration - self.term.minute)/60)
        start_minute = (self.term.minute-self.term.duration)%60
        if Term(self.term.day, start_hour, start_minute, self.term.duration).is_valid() \
        and Term(self.term.day,start_hour,start_minute,self.term.duration).is_full_time() == self.fullTime:
            self.term = Term(self.term.day, start_hour, start_minute, self.term.duration)
            return True
        return False

if __name__ == '__main__':
    lesson = Lesson(Term(Day.THU,8,0),"Programowanie Skryptowe","Stanisław Polak",2)
    print(lesson)
    while lesson.earlierTime():
        print(lesson)
    print("break")
    while lesson.laterDay():
        print(lesson)
    print("break")
    while lesson.laterTime():
        print(lesson)
    print("break")
    while lesson.earlierDay():
        print(lesson)
