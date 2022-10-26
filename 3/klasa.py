import sys
##################################
def color(id):
    return id%7+31
##################################
class Klasa(object):
    tab = [1,2,3]
    def __init__(self, tab, zmienna1, zmienna2):
        self.tab = tab
        self._zmienna1 = zmienna1
        self.__zmienna2 = zmienna2
        print("Wywołano metodę '{}()' obiektu\t\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self)))

    def __del__(self):
        print("Wywołano metodę '{}()' obiektu\t\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self)))

    def metodaInstancyjna(self):
        print(f"self.tab = {self.tab}")
        print(f"Klasa.tab = {Klasa.tab}")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę '{}()' klasy\t\t'{}'".format(sys._getframe().f_code.co_name, cls.__name__))

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę '{}()' klasy\t'{}'".format(sys._getframe().f_code.co_name, __class__.__name__))

print("Załadowano zawartość pliku '{}'".format(__file__))
