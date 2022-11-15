from typing import List
from day import Day,days
from term import Term,days,BasicTerm
from lesson import Lesson
from action import Action
from Break import Break
from BasicTimetable import BasicTimetable, generateTerms, breaks, times

class TimetableWithBreaks(BasicTimetable):
    def __init__(self, breaks: List[Break], skipBreaks=True):
        self.table = {}
        self.number_of_lessons = 0
        self.breaks = breaks
        self.skipBreaks = skipBreaks

    def __str__(self):
        table = [[ [' '] for x in range(7)] for y in range(8)]
        for k,v in self.table.items():
            d = k//1440
            t = k%1440//100-5
            table[d][t].pop()
            table[d][t].append(v)
        s = ""
        s+=f"{105*'*'}\n"
        s+=f"*{' '*11} "
        for i in range(0,7):
            s+=f"*{days[i]:^12}"
        s+="*\n"
        for i in range(0, 7):
            s+=f'{105*"*"}\n*{times[i]:^12}*{str(table[i][0][0]):^12}*{str(table[i][1][0]):^12}*{str(table[i][2][0]):^12}*{str(table[i][3][0]):^12}*{str(table[i][4][0]):^12}*{str(table[i][5][0]):^12}*{str(table[i][6][0]):^12}*\n'
            s+=f"*{104*'*'}\n*{str(self.breaks[i].getTerm()):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*\n"
        #s+=f'{105*"*"}\n*{times[7]:^12}*{str(self.table[7][0][0]):^12}*{str(self.table[7][1][0]):^12}*{str(self.table[7][2][0]):^12}*{str(self.table[7][3][0]):^12}*{str(self.table[7][4][0]):^12}*{str(self.table[7][5][0]):^12}*{str(self.table[7][6][0]):^12}*\n'
        s+=f"{105*'*'}"
        return s

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if self.busy(term):
            return False
        if fullTime:
            if term.day_value > 4 or term.hour < 8 or term.end_hour > 20:
                return False
            if term.day_value == 4 and term.hour > 7:
                if term.end_hour > 17:
                    return False
                elif term.end_hour == 17:
                    if term.end_minute != 0:
                        return False
        else:
           if term.day_value < 4 or term.end_hour < 8 or term.end_hour > 20:
               return False
           if term.day_value == 4:
               if term.hour < 17:
                   return False
        return True

    def busy(self, term: Term) -> bool:
        h = hash(term)
        for k,v in self.table.items():
            if k == h:
                raise ValueError("Term is busy!")
            if k < h and k + v.term.duration > h:
                raise ValueError("Term is busy!")
            if k > h and h + term.duration > k:
                raise ValueError("Term is busy!")
        return False

if __name__ == '__main__':
    s = "t+" 
    tt = TimetableWithBreaks(breaks)
    lesson = Lesson(tt,Term(Day.MON,8,0),"Trzeci","Stanisław Polak",2)
    lesson1 = Lesson(tt,Term(Day.WED,9,40),"Drugi","Stanisław Polak",2)
    lesson3 = Lesson(tt,Term(Day.FRI,8,0),"Pierwszy","Stanisław Polak",2)
    print(tt.table)
    actions = tt.parse(s.split())
    tt.perform(actions)
    print(tt)
