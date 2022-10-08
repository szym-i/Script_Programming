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

    def test_sum_complex_string(self):
        self.assertEqual(sum(1+9j,'3.5'),4.5+9j)

    def test_sum_fraction_integer(self):
        self.assertEqual(sum(Fraction(6/10),1),8/5)

    def test_sum_fraction_float(self):
        self.assertEqual(sum(4.1,Fraction(5/10)),4.6)

    def test_sum_fraction_string(self):
        self.assertEqual(sum(Fraction(2,8),'1.1'),1.35)
    
    def test_sum_fraction_complex(self):
        self.assertEqual(sum(5+2j,Fraction(2/4)),5.5+2j)

    def test_sum_fraction_fraction(self):
        self.assertEqual(sum(Fraction(11/33),Fraction(1/3)),2/3)

    def test_sum_bad_string_integer(self):
        with self.assertRaises(ValueError):
            sum(2,'Ala ma kota123') 

    def test_sum_list_integer(self):
        with self.assertRaises(ValueError):
            sum(1,[2,3])

if __name__ == '__main__':
    unittest.main()
