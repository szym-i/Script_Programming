from DeanerySystem.day import Day
from DeanerySystem.term import *

years = ["0","Pierwszy","Drugi","Trzeci","Czwarty"]
full_time = ["zaocznych","stacjonarnych"]

class Lesson:
    def __init__(self, term: Term, lesson_name: str, teacherName: str, year: int):
        self.__term = term
        self.__name = lesson_name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = self.term.is_full_time()

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self,var):
        self.__term = var

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,var):
        self.__name = var

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self,var):
        self.__teacherName = var

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,var):
        self.__year = var

    @property
    def fullTime(self):
        return self.__fullTime

    @fullTime.setter
    def fullTime(self,var):
        self.__fullTime = var



    def __str__(self):
        return f'{self.name} {self.term}\n{years[self.year]} rok studiów {full_time[self.fullTime]}\nProwadzący: {self.teacherName}'

    def laterDay(self):
        if Term(Day((self.term.day_value+1)%7),self.term.hour,self.term.minute,self.term.duration).is_full_time() != self.fullTime:
            return False
        self.term.day = Day((self.term.day_value+1)%7)
        return True
    
    def earlierDay(self):
        if Term(Day((self.term.day_value-1)%7),self.term.hour,self.term.minute,self.term.duration).is_full_time() != self.fullTime:
            return False
        self.term.day = Day((self.term.day_value-1)%7)
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
