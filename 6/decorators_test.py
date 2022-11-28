from decorators import Operacje
import unittest

class test_decorators(unittest.TestCase):
    def test_sum(self):
        op = Operacje()
        self.assertEqual(op.suma(1,2,3), 6)
        self.assertEqual(op.suma(1,2), 7)
        self.assertEqual(op.suma(1), 10)
        
        with self.assertRaises(TypeError):
            op.suma()
            
        op['suma'] = [99, 1]
        
        self.assertEqual(op.suma(0), 100)
        
    def test_roznica(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 1)
        self.assertEqual(op.roznica(2), -2)
        self.assertEqual(op.roznica(),6)
        self.assertEqual(op.roznica(2, 1),1)

        with self.assertRaises(TypeError):
            op.roznica(1,1,1)
        
        op['roznica'] = [39, 11, 12]
        self.assertEqual(op.roznica(), 12)

    def test__setitem__(self):
        op = Operacje()
        with self.assertRaises(ValueError):
            op['aa'] = ['a','b']

if __name__ == '__main__':
    unittest.main()
