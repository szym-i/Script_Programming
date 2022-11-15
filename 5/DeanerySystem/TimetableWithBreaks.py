from typing import List
from day import Day,days
from term import Term,days,BasicTerm
from lesson import Lesson
from action import Action
from Break import Break
from BasicTimetable import BasicTimetable, generateTerms, breaks, times, NotEnoughLessonsError, FullTimeStudentError

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
            t = (k%1440-480)//100
            if table[t][d] == [' ']:
                table[t][d].pop()
                table[t][d].append(v)
            else:
                table[t][d].append(v)
        s = ""
        s+=f"{105*'*'}\n"
        s+=f"*{' '*11} "
        for i in range(0,7):
            s+=f"*{days[i]:^12}"
        s+="*\n"
        for i in range(0, 7):
            s+=f'{105*"*"}\n*{times[i]:^12}*{str(",".join(map(str,table[i][0]))):^12}*{str(",".join(map(str,table[i][1]))):^12}*{str(",".join(map(str,table[i][2]))):^12}*{str(",".join(map(str,table[i][3]))):^12}*{str(",".join(map(str,table[i][4]))):^12}*{str(",".join(map(str,table[i][5]))):^12}*{str(",".join(map(str,table[i][6]))):^12}*\n'
            s+=f"*{104*'*'}\n*{str(self.breaks[i].getTerm()):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*\n"
        s+=f"{105*'*'}"
        return s

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        self.busy(term) #jeśli będzie busy, wywali wyjątek
        if fullTime:
            if term.day_value > 4 or term.hour < 8 or term.end_hour > 20:
                raise FullTimeStudentError("Fulltime student need to drink beer during weekend")
            if term.day_value == 4 and term.hour > 7:
                if term.end_hour > 17:
                    raise FullTimeStudentError("Fulltime student need to drink beer during weekend")
                elif term.end_hour == 17:
                    if term.end_minute != 0:
                        raise FullTimeStudentError("Fulltime student need to drink beer during weekend")
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
    s = "d+ d+ d+ d+ d+ d+"  
    tt = TimetableWithBreaks(breaks, True)
    lesson = Lesson(tt,Term(Day.MON,8,0,30),"PS","Stanisław Polak",2)
    #lesson1 = Lesson(tt,Term(Day.MON,8,30,60),"Krypto","Stanisław Polak",2)
    actions = tt.parse(s.split())
    tt.perform(actions)
    print(tt)
