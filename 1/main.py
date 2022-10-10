#import main
import cmath
from fractions import Fraction

def sum(arg1, arg2):
    try:
        return complex(arg1) + complex(arg2)
    except:
        raise ValueError

if __name__ == '__main__':
    a = 1+1j
    b = Fraction(2/4)
    print(f"sum({a},{b}) = {sum(a,b)}")
    print(f"__name__ = {__name__}")
