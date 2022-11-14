from TimetableWithBreaks import *
import unittest
from Break import Break

less1 = Lesson(None,Term(Day.MON,8,0),"Fizyka","",2)
less2 = Lesson(None,Term(Day.WED,18,30),"Skryptowe","",2)
less3 = Lesson(None,Term(Day.SUN,9,30),"Kryptografia","",2)
less4 = Lesson(None,Term(Day.SUN,21,30),"AaAA","",1)

class Test_TestTable(unittest.TestCase):

    def test_busy(self):
        tt = TimetableWithBreaks(breaks)
        tt.table[0][0].pop()
        tt.table[0][0].append(less1) 
        term1 = Term(Day.MON,8,0)
        term2 = Term(Day.MON,12,30)
        term3 = Term(Day.SAT,11,10)
        self.assertEqual(tt.busy(term1),True)
        self.assertEqual(tt.busy(term2),False)
        self.assertEqual(tt.busy(term3),False)

    def test_can_be_transferred(self):
        tt = TimetableWithBreaks(breaks)
        tt.put(less1) 
        term1 = Term(Day.MON,11,0)
        term2 = Term(Day.MON,12,30)
        term3 = Term(Day.SAT,11,10)
        self.assertEqual(tt.can_be_transferred_to(term1,True),True)
        self.assertEqual(tt.can_be_transferred_to(term1,False),False)
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
        #self.assertRaises(ValueError,tt.parse(s1))
        #self.assertRaises(ValueError,tt.parse(s2))
        with self.assertRaises(ValueError) as context:
            tt.parse(s1)
        print(str(context.exception))
        self.assertTrue('ValueError: 123 is not a valid Action' in str(context.exception))
    
    def test_perform(self):
        tt = TimetableWithBreaks(breaks)
        less1 = Lesson(tt,Term(Day.MON,12,30),"Fizyka","",1)
        less2 = Lesson(tt,Term(Day.WED,18,30),"Skryptowe","",1)
        res1 = [Action.DAY_LATER,Action.TIME_LATER,Action.DAY_LATER,Action.TIME_EARLIER]
        newtable = TimetableWithoutBreaks()
        less3 = Lesson(newtable,Term(Day.WED,12,30),"Fizyka","",1)
        less4 = Lesson(newtable,Term(Day.WED,17,0),"Skryptowe","",1)
        tt.perform(res1)
        self.assertEqual(str(tt),str(newtable))
    
    def test_str(self):
        tt = TimetableWithBreaks(breaks)
        less1 = Lesson(tt,Term(Day.MON,8,0),"Fizyka","",1)
        less2 = Lesson(tt,Term(Day.WED,8,0),"Skryptowe","",1)
        less3 = Lesson(tt,Term(Day.WED,9,30),"Kryptografia","",1)
        result ="""*********************************************************************************************************
*            *Poniedziałek*   Wtorek   *   Środa    *  Czwartek  *   Piątek   *   Sobota   * Niedziela  *
*********************************************************************************************************
* 8:00-9:30  *   Fizyka   *            * Skryptowe  *            *            *            *            *
*********************************************************************************************************
* 9:30-11:00 *            *            *Kryptografia*            *            *            *            *
*********************************************************************************************************
*11:00-12:30 *            *            *            *            *            *            *            *
*********************************************************************************************************
*12:30-14:00 *            *            *            *            *            *            *            *
*********************************************************************************************************
*14:00-15:30 *            *            *            *            *            *            *            *
*********************************************************************************************************
*15:30-17:00 *            *            *            *            *            *            *            *
*********************************************************************************************************
*17:00-18:30 *            *            *            *            *            *            *            *
*********************************************************************************************************
*18:30-20:00 *            *            *            *            *            *            *            *
*********************************************************************************************************"""
        self.assertEqual(str(tt),result)
    

if "__main__" == __name__:
    unittest.main()
