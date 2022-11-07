from day import Day
from term import Term,days
import math

times = ["8:00-9:30","9:30-11:00","11:00-12:30","12:30-14:00","14:00-15:30","15:30-17:00","17:00-18:30","18:30-20:00"]
years = ["0","Pierwszy","Drugi","Trzeci","Czwarty"]
full_time = ["zaocznych","stacjonarnych"]

class Lesson:
    def __init__(self,timetable, term: Term, lesson_name: str, teacherName: str, year: int):
        self.__timetable = timetable
        self.__term = term
        self.__name = lesson_name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = self.term.is_full_time()
        timetable.put(self)
        timetable.number_of_lessons+=1
    
    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self,var):
        self.__timetable = var


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
        return f'{self.name}'

    def laterDay(self):
        possible_term = Term(Day((self.term.day_value+1)%7),self.term.hour,self.term.minute,self.term.duration)
        if possible_term.is_full_time() == self.fullTime and self.timetable.can_be_transferred_to(possible_term,self.fullTime):
            day, time = str(self.term).split()
            #if day in days and time in times:
            t = times.index(time)
            d = days.index(day)
            self.timetable.table[t][d].pop()
            self.timetable.table[t][d].append(' ')
            self.term.day = Day((self.term.day_value+1)%7)
            self.timetable.put(self)
            return True
        return False
    
    def earlierDay(self):
        possible_term = Term(Day((self.term.day_value-1)%7),self.term.hour,self.term.minute,self.term.duration)
        if possible_term.is_full_time() == self.fullTime and self.timetable.can_be_transferred_to(possible_term,self.fullTime):
            day, time = str(self.term).split()
            #if day in days and time in times:
            t = times.index(time)
            d = days.index(day)
            self.timetable.table[t][d].pop()
            self.timetable.table[t][d].append(' ')
            self.term.day = Day((self.term.day_value-1)%7)
            self.timetable.put(self)
            return True
        return False

    def laterTime(self):
        start_hour = (self.term.hour + (self.term.duration+self.term.minute)//60)%24
        start_minute = (self.term.minute + self.term.duration%60)%60
        if Term(self.term.day,start_hour,start_minute,self.term.duration).is_valid()\
        and Term(self.term.day,start_hour,start_minute,self.term.duration).is_full_time() == self.fullTime:
            possible_term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
                day, time = str(self.term).split()
                t = times.index(time)
                d = days.index(day)
                self.timetable.table[t][d].pop()
                self.timetable.table[t][d].append(' ')
                self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
                self.timetable.put(self)
                return True
        return False

    def earlierTime(self):
        start_hour = self.term.hour - math.ceil((self.term.duration - self.term.minute)/60)
        start_minute = (self.term.minute-self.term.duration)%60
        if Term(self.term.day, start_hour, start_minute, self.term.duration).is_valid() \
        and Term(self.term.day,start_hour,start_minute,self.term.duration).is_full_time() == self.fullTime:
            possible_term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
                day, time = str(self.term).split()
                t = times.index(time)
                d = days.index(day)
                self.timetable.table[t][d].pop()
                self.timetable.table[t][d].append(' ')
                self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
                self.timetable.put(self)
                return True
        return False
