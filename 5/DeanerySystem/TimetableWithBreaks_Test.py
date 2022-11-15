import unittest
from TimetableWithBreaks import *
from Break import Break
from day import Day,days

less1 = Lesson(None,Term(Day.MON,8,0),"Fizyka","",2)
less2 = Lesson(None,Term(Day.WED,8,0),"Skryptowe","",2)
less3 = Lesson(None,Term(Day.SUN,8,0),"Kryptografia","",2)
less4 = Lesson(None,Term(Day.SAT,8,0),"AaAA","",1)

class Test_TimeTable(unittest.TestCase):

    def test_busy(self):
        tt = TimetableWithBreaks(breaks)
        tt.put(less1) 
        term1 = Term(Day.MON,8,0)
        term2 = Term(Day.MON,9,40)
        term3 = Term(Day.SAT,11,20)
        with self.assertRaises(ValueError):
            tt.busy(term1)
        self.assertEqual(tt.busy(term2),False)
        self.assertEqual(tt.busy(term3),False)

    def test_can_be_transferred(self):
        tt = TimetableWithBreaks(breaks)
        tt.put(less1) 
        term1 = Term(Day.MON,8,0)
        term2 = Term(Day.WED,8,0)
        term3 = Term(Day.SAT,8,0)
        with self.assertRaises(ValueError):
            tt.can_be_transferred_to(term1,True)
        with self.assertRaises(ValueError):
            tt.can_be_transferred_to(term1,False)
        self.assertEqual(tt.can_be_transferred_to(term2,True),True)
        self.assertEqual(tt.can_be_transferred_to(term3,False),True)
    
    def test_put(self):
        tt = TimetableWithBreaks(breaks)
        self.assertEqual(tt.put(less1),True)
        self.assertEqual(tt.put(less2),True)
        self.assertEqual(tt.put(less3),True)
    
    def test_get(self):
        tt = TimetableWithBreaks(breaks)
        tt.put(less1)
        tt.put(less2)
        tt.put(less3)
        self.assertEqual(tt.get(less1.term),less1)
        self.assertEqual(tt.get(less2.term),less2)
        self.assertEqual(tt.get(less3.term),less3)
        self.assertEqual(tt.get(less4.term),None)
    
    def test_parse(self):
        tt = TimetableWithBreaks(breaks)
        s1 = ["d+",123,"df","t+"]
        res1 = [Action.DAY_LATER,Action.TIME_LATER]
        s2 = ["d+","d-","df","t-","t+"]
        res2 = [Action.DAY_LATER,Action.DAY_EARLIER,Action.TIME_EARLIER,Action.TIME_LATER]
        with self.assertRaises(ValueError):
            tt.parse(s1)
        with self.assertRaises(ValueError):
            tt.parse(s2)
    
    def test_perform(self):
        tt = TimetableWithBreaks(breaks)
        act = [Action.DAY_LATER,Action.TIME_LATER,Action.DAY_LATER,Action.TIME_EARLIER]
        with self.assertRaises(ZeroDivisionError):
            tt.perform(act)
        less1 = Lesson(tt,Term(Day.MON,8,0),"Fizyka","",1)
        less2 = Lesson(tt,Term(Day.WED,9,40),"Skryptowe","",1)
        tt.perform(act)
        newtable = TimetableWithBreaks(breaks)
        less3 = Lesson(newtable,Term(Day.MON,8,0),"Fizyka","",1)
        less4 = Lesson(newtable,Term(Day.WED,9,40),"Skryptowe","",1)
        newtable.perform(act)
        #self.assertEqual(str(tt),str(newtable))
    
    def test_str(self):
        return 0
        tt = TimetableWithBreaks(breaks)
        less1 = Lesson(tt,Term(Day.MON,8,0),"Fizyka","",1)
        less2 = Lesson(tt,Term(Day.WED,8,0),"Skryptowe","",1)
        less3 = Lesson(tt,Term(Day.WED,9,40),"Kryptografia","",1)
        result = "*********************************************************************************************************\n*            *Poniedziałek*   Wtorek   *   Środa    *  Czwartek  *   Piątek   *   Sobota   * Niedziela  *\n*********************************************************************************************************\n* 8:00-9:30  *   Fizyka   *            * Skryptowe  *            *            *            *            *\n*********************************************************************************************************\n* 9:30-9:40  *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n* 9:40-11:10 *            *            *Kryptografia*            *            *            *            *\n*********************************************************************************************************\n*11:10-11:20 *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n*11:20-12:50 *            *            *            *            *            *            *            *\n*********************************************************************************************************\n*12:50-13:00 *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n*13:00-14:30 *            *            *            *            *            *            *            *\n*********************************************************************************************************\n*14:30-14:40 *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n*14:40-16:10 *            *            *            *            *            *            *            *\n*********************************************************************************************************\n*16:10-16:20 *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n*16:20-17:50 *            *            *            *            *            *            *            *\n*********************************************************************************************************\n*17:50-18:00 *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n*18:00-19:30 *            *            *            *            *            *            *            *\n*********************************************************************************************************\n*19:30-19:40 *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *    ---     *\n*********************************************************************************************************\n*19:40-21:10 *            *            *            *            *            *            *            *\n*********************************************************************************************************"
        self.assertEqual(str(tt),result)
    

if "__main__" == __name__:
    unittest.main()
