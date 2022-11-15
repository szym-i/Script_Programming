from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from day import Day, days
import math
from lesson import Lesson
from action import Action
from term import BasicTerm,Term
from Break import Break
from sortedcontainers import SortedDict


def generateTerms(breaks: List[Break]):
    if len(breaks) != 7:
        return "Enter exactly 7 breaks" 
    terms = []
    sh = 8
    sm = 0
    for i in range(0,7):
        eh = breaks[i].hour
        em = breaks[i].minute
        if sm < 10 and em < 10:
            terms.append(f'{sh}:0{str(sm)}-{eh}:0{em}')
        elif sm < 10:
            terms.append(f'{sh}:0{str(sm)}-{eh}:{em}')
        elif em < 10:
            terms.append(f'{sh}:{str(sm)}-{eh}:0{em}')
        else:
            terms.append(f'{sh}:{sm}-{eh}:{em}')
        sh = breaks[i].end_hour
        sm = breaks[i].end_minute
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

breaks = [Break(9,30,10), Break(11,10,10), Break(12,50,10), Break(14,30,10), Break(16,10,10), Break(17,50,10), Break(19,30,10)]
times = generateTerms(breaks)


class BasicTimetable(ABC):
    @abstractmethod
    def busy(self, term: Term) -> bool:
        pass

    def get(self, term: Term) -> Lesson:
        if hash(term) in self.table.keys():
            return self.table[hash(term)]
        return None
    
    def parse(self, actions: List[str]) -> List[Action]:
        result = []
        for e in actions:
            try:
                result.append(Action(e))
            except:
                raise ValueError(f"Translation {e} is incorrect")
        return result

    def perform(self, actions: List[Action]):
        if len(self.table) == 0:
            raise ZeroDivisionError
        for i in range(1,len(actions)+1):
            l = self.find_nth_lesson((i-1)%len(self.table))
            if actions[i-1] == Action("d+"):
                l.laterDay(self.skipBreaks)
            if actions[i-1] == Action("d-"):
                l.earlierDay(self.skipBreaks)
            if actions[i-1] == Action("t+"):
                l.laterTime(self.skipBreaks)
            if actions[i-1] == Action("t-"):
                l.earlierTime(self.skipBreaks)
    
    def put(self, lesson: Lesson) -> bool:
        self.table[hash(lesson.term)] = lesson
        self.table = { k: v for k,v in sorted(self.table.items())}
        return True

    def find_nth_lesson(self,n):
        if n < 0:
            return f"Use n >= 0 {n}"
        x = 0
        for l in self.table.values():
            if x == n:
                return l
            x+=1

class Timetable(BasicTimetable):
    def parse(self, actions):
        pass
    def perform(self, actions):
        pass
    def busy(self, term):
        pass
    def put(self):
        pass
