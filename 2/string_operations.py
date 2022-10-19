#-*-coding: utf-8-*-

lancuch1 = '''Pierwsza linijka lancuch1
druga linijka lancuch1 '''
lancuch2 = '''Pierwsza linijka lancuch2
druga linijka lancuch2 '''
lancuch = "123456789"

if __name__ == '__main__':
    print(f"Lancuch1:\n{lancuch1}")
    print(f"Lancuch2:\n {lancuch2}")
    print("3*(lancuch1+lancuch2):",3*(lancuch1+lancuch2))
    print("Lancuch =",lancuch)
    print("Pierwszy znak lancucha:",lancuch[0])
    print("Dwa pierwsze znaki lancucha:",lancuch[:2])
    print("Wszystkie znaki za wyjątkiem dwóch pierwszych:",lancuch[2:])
    print("Przedostatni znak lancucha:",lancuch[-2])
    print("Trzy ostatnie znaki:",lancuch[len(lancuch)-3:])
    print("Wszystkie znaki na parzystych pozycjach(licząc od 1):",lancuch[1::2])
    try:
        lancuch[0] = "a"
    except:
        print("Łańcuchy znaków NIE mogą być modyfikowane")
