from main import sum, Fraction
import unittest


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(sum(2, '2'), 4)

    def test_sum_string_string(self):
         self.assertEqual(sum('2.1', '2.0'), 4.1)

    def test_sum_complex_integer(self):
        self.assertEqual(sum(2+1j,2),4+1j)

    def test_sum_complex_complex(self):
        self.assertEqual(sum(4+2j,2+1j),6+3j)
    
    def test_fraction_complex(self):
        self.assertEqual(sum(5+2j,Fraction(2/4)),5.5+2j)

    def test_fraction_fraction(self):
        self.assertEqual(sum(Fraction(11/33),Fraction(1/3)),2/3)

    def test_bad_string_integer(self):
        with self.assertRaises(ValueError):
            sum(2,'Ala ma kota123') 

    def test_list_integer(self):
        with self.assertRaises(ValueError):
            sum(1,[2,3])

if __name__ == '__main__':
    unittest.main()
