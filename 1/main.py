#import main
import cmath
from fractions import Fraction

def sum(arg1, arg2):
    try:
        if isinstance(arg1,str): # to po to, aby móc używać ułamków w postaci stringa np. sum('1/2',1)
            if '/' in arg1:
                arg1 = Fraction(arg1)
            else:
                arg1 = complex(arg1)
        if isinstance(arg2,str):
            if '/' in arg2:
                arg2 = Fraction(arg2)
            else:
                arg2 = complex(arg2)
        return arg1 + arg2
    except:
        raise ValueError

if __name__ == '__main__':
    a = '1+1j'
    b = '1/2'
    print(f"sum({a},{b}) = {sum(a,b)}")
    print(f"__name__ = {__name__}")
