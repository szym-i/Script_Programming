from typing import List
from day import Day
from term import Term,days
from with_timetable_lesson import Lesson
from action import Action


times = ["8:00-9:30","9:30-11:00","11:00-12:30","12:30-14:00","14:00-15:30","15:30-17:00","17:00-18:30","18:30-20:00"]

class TimetableWithoutBreaks(object):
    def __init__(self):
        self.table = [[ [' '] for x in range(7)] for y in range(8)]
        self.number_of_lessons = 0

    def __str__(self):
        print(f"{105*'*'}")
        print(f"*{' '*11} ",end="")
        for i in range(0,7):
            print(f"*{days[i]:^12}",end="")
        print("*")
        for i in range(0, 8):
            print(f'{105*"*"}\n*{times[i]:^12}*{str(self.table[i][0][0]):^12}*{str(self.table[i][1][0]):^12}*{str(self.table[i][2][0]):^12}*{str(self.table[i][3][0]):^12}*{str(self.table[i][4][0]):^12}*{str(self.table[i][5][0]):^12}*{str(self.table[i][6][0]):^12}*')
        print(f"{105*'*'}")

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if self.busy(term):
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
                return True
            return "The lesson cannot be placed if the timetable is already occupied"
        return "The lesson term is incorrect"

    def parse(self, actions: List[str]) -> List[Action]:
        result = []
        for e in actions:
            try:
                result.append(Action(e))
            except:
                pass
        self.perform(result)
        #return result

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
    import sys
    s = "t+ t+ t+ t+ t- t- t- t- t-"
    tt = TimetableWithoutBreaks()
    #lesson = Lesson(tt,Term(Day.THU,8,0),"Trzeci","Stanisław Polak",2)
    #lesson1 = Lesson(tt,Term(Day.WED,8,0),"Drugi","Stanisław Polak",2)
    lesson3 = Lesson(tt,Term(Day.WED,9,30),"Pierwszy","Stanisław Polak",2)
    tt.__str__()
    tt.parse(s.split())
    tt.__str__()
