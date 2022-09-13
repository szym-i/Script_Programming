lancuch1 = "aa aa\na"
lancuch2 = "bbb\nb"
lancuch = "Mianem back-endu określa się technologie webowe, których kody źródłowe wykonywane są przez procesor serwera"


if __name__ == '__main__':
    print("Lancuch1 =",lancuch1)
    print("Lancuch2 =",lancuch2)
    print("Lancuch =",lancuch)
    print("3*(lancuch1+lancuch2):",3*(lancuch1+lancuch2))
    print("Pierwszy znak lancucha:",lancuch[0])
    print("Dwa pierwsze znaki lancucha:",lancuch[:2])
    print("Wszystkie znaki za wyjątkiem dwóch pierwszych:",lancuch[2:])
    print("Przedostatni znak lancucha:",lancuch[-2])
    print("Trzy ostatnie znaki:",lancuch[len(lancuch)-3:])
    print("Wszystkie znaki na parzystych pozycjach(licząc od 1):",lancuch[1::2])
