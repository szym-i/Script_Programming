import sys
from math import sqrt

def if_prime(n):
    try:
        n = int(n)
        if n == 1:
            return False
        if n % 2 == 0 and n != 2:
            return False
        for i in range(3,int(sqrt(n))+1,2):
            if n % i == 0:
                return False
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    x = len(sys.argv)
    print(f"Total arguments passed {x-1}")
    for i in range(1,x):
        if if_prime(sys.argv[i]) == True:
            print(sys.argv[i])
