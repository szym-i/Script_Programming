from term import Term
from day import Day, days
import math

times = ["8:00-9:30","9:40-11:10","11:20-12:50","13:00-14:30","14:40-16:10","16:20-17:50","18:00-19:30","19:40-21:10"]
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
        if timetable != None:
            timetable.put(self)
    
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

    def __repr__(self):
        return f'{self.name} {self.term}'

    def laterDay(self,skipBreaks):
        possible_term = Term(Day((self.term.day_value+1)%7),self.term.hour,self.term.minute,self.term.duration)
        if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
            self.timetable.table.pop(hash(self.term))
            self.term.day = Day((self.term.day_value+1)%7)
            self.timetable.put(self)
            return True
        return False
    
    def earlierDay(self,skipBreaks):
        possible_term = Term(Day((self.term.day_value-1)%7),self.term.hour,self.term.minute,self.term.duration)
        if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
            day, time = str(self.term).split()
            t = times.index(time)
            d = days.index(day)
            self.timetable.table[t][d].pop()
            self.timetable.table[t][d].append(' ')
            self.timetable.number_of_lessons-=1
            self.term.day = Day((self.term.day_value-1)%7)
            self.timetable.put(self)
            return True
        return False

    def laterTime(self, skipBreaks = False):
        break_duration = 0
        if skipBreaks:
            break_duration = 10
        start_hour = (self.term.hour + (self.term.duration+self.term.minute+break_duration)//60)%24
        start_minute = (self.term.minute + self.term.duration%60 + break_duration)%60
        possible_term = Term(self.term.day,start_hour,start_minute,self.term.duration)
        if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
            self.timetable.table.pop(hash(self.term))
            self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            self.timetable.put(self)
            return True
        return False

    def earlierTime(self, skipBreaks = False):
        break_duration = 0
        if skipBreaks:
            start_hour = self.term.hour - math.ceil((self.term.duration - self.term.minute-break_duration)/60)
            start_minute = (self.term.minute-self.term.duration-break_duration)%60
            possible_term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
                self.timetable.table.pop(hash(self.term))
                self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
                self.timetable.put(self)
                return True
            return False
        else:
            day, time = str(self.term).split()
            t = times.index(time)
            d = days.index(day)
            break_duration = 10
            start_hour = self.term.hour - math.ceil((self.term.duration - self.term.minute-break_duration)/60)
            start_minute = (self.term.minute-self.term.duration-break_duration)%60
            possible_term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
            if self.timetable.can_be_transferred_to(possible_term,self.fullTime):
                self.timetable.table[t][d].pop()
                self.timetable.table[t][d].append(' ')
                self.timetable.number_of_lessons-=1
                self.term = Term(self.term.day,start_hour,start_minute,self.term.duration) 
                self.timetable.put(self)
                return True
            return False
