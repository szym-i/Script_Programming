class Reader:

    def __init__(self, name, surname, pesel):
        self.__name = name
        self.__surname = surname
        self.__pesel = pesel

    def __str__(self):
        return f'{self.__name} {self.__surname}'

if __name__ == '__main__':
    r1 = Reader("Bomasz","Tojdys",3198591384121)
    print(r1)
