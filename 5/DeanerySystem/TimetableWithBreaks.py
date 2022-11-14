from typing import List
from day import Day
from term import Term,days
from lesson import Lesson
from action import Action
from Break import Break

breaks = [Break(Term(None,9,30,10)), Break(Term(None,11,10,10)), Break(Term(None,12,50,10)), Break(Term(None,14,30,10)), Break(Term(None,16,10,10)), Break(Term(None,17,50,10)), Break(Term(None,19,30,10))]

#times = ["8:00-9:30","9:40-11:10","11:20-12:50","13:00-14:30","14:40-16:10","16:20-17:50","18:00-19:30","19:40-21:10"]

def generateTerms(breaks: List[Break]):
    if len(breaks) != 7:
        return "Enter exactly 7 breaks" 
    terms = []
    sh = 8
    sm = 0
    for i in range(0,7):
        eh = breaks[i].term.hour
        em = breaks[i].term.minute
        if sm < 10 and em < 10:
            terms.append(f'{sh}:0{str(sm)}-{eh}:0{em}')
        elif sm < 10:
            terms.append(f'{sh}:0{str(sm)}-{eh}:{em}')
        elif em < 10:
            terms.append(f'{sh}:{str(sm)}-{eh}:0{em}')
        else:
            terms.append(f'{sh}:{sm}-{eh}:{em}')
        sh = breaks[i].term.end_hour
        sm = breaks[i].term.end_minute
    eh = sh + (sm + 90)//60
    em = (sm + 90)%60
    if sm < 10 and em < 10:
        terms.append(f'{sh}:0{str(sm)}-{eh}:0{em}')
    elif sm < 10:
        terms.append(f'{sh}:0{str(sm)}-{eh}:{em}')
    elif em < 10:
        terms.append(f'{sh}:{str(sm)}-{eh}:0{em}')
    else:
        terms.append(f'{sh}:{sm}-{eh}:{em}')
    return terms

class TimetableWithBreaks(object):
    def __init__(self, breaks: List[Break]):
        self.table = [[ [' '] for x in range(7)] for y in range(8)]
        self.number_of_lessons = 0
        self.breaks = breaks

    def __str__(self):
        s = ""
        s+=f"{105*'*'}\n"
        s+=f"*{' '*11} "
        for i in range(0,7):
            s+=f"*{days[i]:^12}"
        s+="*\n"
        for i in range(0, 7):
            s+=f'{105*"*"}\n*{times[i]:^12}*{str(self.table[i][0][0]):^12}*{str(self.table[i][1][0]):^12}*{str(self.table[i][2][0]):^12}*{str(self.table[i][3][0]):^12}*{str(self.table[i][4][0]):^12}*{str(self.table[i][5][0]):^12}*{str(self.table[i][6][0]):^12}*\n'
            s+=f"*{104*'*'}\n*{str(self.breaks[i].getTerm()):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*{str(breaks[i]):^12}*\n"
        s+=f'{105*"*"}\n*{times[7]:^12}*{str(self.table[7][0][0]):^12}*{str(self.table[7][1][0]):^12}*{str(self.table[7][2][0]):^12}*{str(self.table[7][3][0]):^12}*{str(self.table[7][4][0]):^12}*{str(self.table[7][5][0]):^12}*{str(self.table[7][6][0]):^12}*\n'
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
        day, time = str(term).split()
        if day in days and time in times:
            t = times.index(time)
            d = days.index(day)
            if self.table[t][d][0] != ' ':
                return True
        return False

    def put(self, lesson: Lesson) -> bool:
        day, time = str(lesson.term).split()
        if day in days and time in times:
            t = times.index(time)
            d = days.index(day)
            if self.table[t][d][0] == ' ':
                self.table[t][d].pop()
                self.table[t][d].append(lesson)
                self.number_of_lessons+=1
                return True
            return "The lesson cannot be placed if the timetable is already occupied"
        return "The lesson term is incorrect"

    def parse(self, actions: List[str]) -> List[Action]:
        result = []
        for e in actions:
            try:
                result.append(Action(e))
            except:
                raise ValueError
        return result

    def perform(self, actions: List[Action]):
        if self.number_of_lessons == 0:
            return "Add some lessons to perform actions"
        for i in range(1,len(actions)+1):
            l = self.find_nth_lesson((i-1)%self.number_of_lessons)
            if actions[i-1] == Action("d+"):
                l.laterDay()
            if actions[i-1] == Action("d-"):
                l.earlierDay()
            if actions[i-1] == Action("t+"):
                l.laterTime()
            if actions[i-1] == Action("t-"):
                l.earlierTime()

    def get(self, term: Term) -> Lesson:
        day, time = str(term).split()
        if day in days and time in times:
            t = times.index(time)
            d = days.index(day)
            if self.table[t][d][0] != ' ':
                return self.table[t][d][0]
        return None

    def find_nth_lesson(self,n):
        if n < 0:
            return f"Use n >= 0 {n}"
        x = 0
        for i in self.table:
            for j in i:
                if j[0] != ' ':
                    if x == n:
                        return j[0]
                    x+=1

if __name__ == '__main__':
    s = "t+ t+ t+ t+ t+ t+ t+ t+ t+ t+ t+ t+ t+"
    times = generateTerms(breaks)
    tt = TimetableWithBreaks(breaks)
    lesson = Lesson(tt,Term(Day.THU,8,0),"Trzeci","Stanisław Polak",2)
    lesson1 = Lesson(tt,Term(Day.WED,8,0),"Drugi","Stanisław Polak",2)
    #lesson3 = Lesson(tt,Term(Day.WED,9,40),"Pierwszy","Stanisław Polak",2)
    print(tt)
    actions = tt.parse(s.split())
    tt.perform(actions)
    print(tt)
