from inspect import signature

def argumenty(argumenty):
    def inner(f):
        def wrapper(*args, **kwargs):
            f_arg = len(signature(f).parameters)
            passed_args = list(args)
            global last
            last = 'pass'
            x = f_arg - len(passed_args)
            if x > len(argumenty):
                raise TypeError(f'{f.__name__}() takes exactly {f_arg} arguments ({len(argumenty) + len(passed_args)} given)')
            if len(passed_args) == 0:
                last = argumenty[f_arg]
            for i in range(0, x):
                passed_args.append(argumenty[i])
            return f(*passed_args)
        return wrapper
    return inner

class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    def __init__(self):
        self.update()

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        pass

    def sumav2(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')
        if last != 'pass':
            return last
        return a + b + c

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        pass
        
    def roznicav2(self, x, y):
        print(f'{x} - {y} = {x - y}')
        if last != 'pass':
            return last
        return x - y
        
    def update(self):
        self.suma = (argumenty(Operacje.argumentySuma))(self.sumav2)
        self.roznica = (argumenty(Operacje.argumentyRoznica))(self.roznicav2)

    def __setitem__(self, key, value):
        if key == 'suma':
            Operacje.argumentySuma = value
        elif key == 'roznica':
            Operacje.argumentyRoznica = value
        else:
            raise ValueError
        self.update()

if __name__ == '__main__':
    op=Operacje()
    op.suma(1,2,3) #Wypisze: 1+2+3=6
    op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
    op.roznica(2,1) #Wypisze: 2-1=1
    op.roznica(2) #Wypisze: 2-4=-2
    wynik=op.roznica() #Wypisze: 4-5=-1
    print(wynik)#Wypisze: 6

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma']=[1,2]
    #oznacza, że   argumentySuma=[1,2]

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica']=[1,2,3]
    op.suma(1)
    #oznacza, że   argumentyRoznica=[1,2,3]
