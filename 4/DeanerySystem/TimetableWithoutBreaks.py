from typing import List
from term import Term,days
from without_timetable_lesson import Lesson
from action import Action


terms = ["8:00-9:30","9:30-11:00","11:00-12:30","12:30-14:00","14:00-15:30","15:30-17:00","17:00-18:30","18:30-20:00"]

class TimetableWithoutBreaks(object):
    def __init__(self):
        self.table = [[' ']*7]*8
        self.number_of_lessons = 0

    def __str__(self):
        print(f"{105*'*'}")
        print(f"*{' '*11} ",end="")
        for i in range(0,7):
            print(f"*{days[i]:^12}",end="")
        print("*")
        for i in range(0, 8):
            print(f'{105*"*"}\n*{terms[i]:12}*{self.table[i][0]:12}*{self.table[i][1]:12}*{self.table[i][2]:12}*{self.table[i][3]:12}*{self.table[i][4]:12}*{self.table[i][5]:12}*{self.table[i][6]:12}*')
        print(f"{105*'*'}")

##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
fullTime : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""
        pass

##########################################################

    def busy(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """
        pass

 ##########################################################

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """
        pass

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """
        result = []
        for e in actions:
            try:
                result.append(Action(e))
            except:
                pass
        return result

##########################################################

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """
        #for i in range(0,self.number_of_lessons):
         #   prin
        pass
##########################################################

    def get(self, term: Term) -> Lesson:
       """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """
    pass

if __name__ == '__main__':
    s = "d+ d- t- t+ d e a "
    tt = TimetableWithoutBreaks()
    a = tt.parse(s.split())
    print(tt)
    #n = 2
    #for i in range(0,len(a)):
        #print(a[i], i % n)
