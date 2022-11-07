from day import Day
from term import Term
from lesson import Lesson
import unittest

lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 2)
lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 2)

class Test_TestDeanerySystem(unittest.TestCase):
    def test_earlierDay(self):
        self.assertFalse(lesson1.earlierDay())
        self.assertFalse(lesson2.earlierDay())
        self.assertTrue(lesson3.earlierDay())
        self.assertFalse(lesson4.earlierDay())
        self.assertTrue(lesson5.earlierDay())

    def test_laterDay(self):
        self.assertTrue(lesson1.laterDay())
        self.assertTrue(lesson2.laterDay())
        self.assertTrue(lesson3.laterDay())
        self.assertTrue(lesson4.laterDay())
        self.assertTrue(lesson5.laterDay())

    def test_laterTime(self):
        self.assertTrue(lesson1.laterTime())
        self.assertTrue(lesson2.laterTime())
        self.assertTrue(lesson3.laterTime())
        self.assertTrue(lesson4.laterTime())
        self.assertTrue(lesson5.laterTime())

    def test_earlierTime(self):
        self.assertFalse(lesson1.earlierTime())
        self.assertTrue(lesson2.earlierTime())
        self.assertTrue(lesson3.earlierTime())
        self.assertTrue(lesson4.earlierTime())
        self.assertFalse(lesson5.earlierTime())

if __name__ == '__main__':
    unittest.main()
