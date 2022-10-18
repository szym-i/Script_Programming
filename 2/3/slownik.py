from collections import Counter

print('Ładowanie modułu "{0}"'.format(__name__))

def wypisz(slownik):
    for key, value in slownik.items():
        print(f"{key}:{value}",end=" ")

def zapisz(arr,slownik):
    slownik.update(Counter(arr)) #jeśli chcemy policzyć wystąpienia argumentów
    #OR
    #a=[]
   # for e in arr:
    #    for c in e:
    #        a.append(c)
    #slownik.update(Counter(a))

print('Załadowano moduł "{0}"'.format(__name__))

slownik = {}
