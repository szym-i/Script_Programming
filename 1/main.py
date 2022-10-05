#import main
import cmath
from fractions import Fraction

def sum(arg1, arg2):
    try:
        arg1 = complex(arg1)
    except:
        return arg2
    try:
        arg2 = complex(arg2)
    except:
        return arg1
    return arg1+arg2
    

if __name__ == '__main__':
    a = 9 + 1j
    b = Fraction(2/4)
    print(b)
    print(f"suma = {sum(a,b)}")
    print(f"__name__ = {__name__}")
