import unittest
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.term import Term


class Test_DeanerySystem(unittest.TestCase):

    def test_nth(self):
        self.assertEqual(nthDayFrom(1, Day.SAT), Day.SUN)
        self.assertEqual(nthDayFrom(2, Day.SAT), Day.MON)
        self.assertEqual(nthDayFrom(-1, Day.TUE), Day.MON)
        self.assertEqual(nthDayFrom(-2, Day.TUE), Day.SUN)

    def test_difference(self):
        self.assertEqual(Day.MON.difference(Day.TUE), 1)
        self.assertEqual(Day.MON.difference(Day.SUN), -1)
        self.assertEqual(Day.SUN.difference(Day.MON), 1)
        self.assertEqual(Day.SUN.difference(Day.SAT), -1)

    def test_earlierThan(self):
        self.assertEqual(Term(Day.MON,9,45).earlierThan(Term(Day.MON,9,45)), False)
        self.assertEqual(Term(Day.MON,10,30).earlierThan(Term(Day.TUE,9,45)), True)
        self.assertEqual(Term(Day.WED,15,5).earlierThan(Term(Day.MON,9,45)), False)
        self.assertEqual(Term(Day.MON,8,0).earlierThan(Term(Day.MON,9,45)), True)

    def test_laterThan(self):
        self.assertEqual(Term(Day.MON,9,45).laterThan(Term(Day.MON,11,45)), False)
        self.assertEqual(Term(Day.MON,9,45).laterThan(Term(Day.MON,9,45)), False)
        self.assertEqual(Term(Day.MON,9,45).laterThan(Term(Day.MON,9,45)), False)
        self.assertEqual(Term(Day.MON,9,45).laterThan(Term(Day.MON,9,45)), False)

    def test_equals(self):
        self.assertEqual(Term(Day.MON,9,45).equals(Term(Day.MON,9,45)), True)
        self.assertEqual(Term(Day.MON,9,45).equals(Term(Day.TUE,9,45)), False)
        self.assertEqual(Term(Day.SUN,11,44).equals(Term(Day.SUN,11,44)), True)
        self.assertEqual(Term(Day.MON,9,45).equals(Term(Day.MON,8,45)), False)


if __name__ == '__main__':
    unittest.main()
