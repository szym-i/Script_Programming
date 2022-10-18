print('Ładowanie modułu "{0}"'.format(__name__))

def wypisz(lista):
    for e in set(lista):
        print(f"{e}:{lista.count(e)}",end=" ")

def zapisz(arr,lista):
    for e in arr:
        lista.append(e)
    #OR
    #for e in arr:
     #   for c in str(e):
      #      lista.append(c)

print('Załadowano moduł "{0}"'.format(__name__))
lista = []
