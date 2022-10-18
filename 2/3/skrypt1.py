import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter --lista/--slownik argument")
        quit()
    print("liczba: liczba_wystąpień")
    match sys.argv[1]:
        case "--slownik":
            import slownik as s
            s.wypisz(s.slownik)
            s.zapisz(sys.argv[2:],s.slownik)
            s.wypisz(s.slownik)
        case  "--lista": 
            import lista as l
            l.wypisz(l.lista)
            l.zapisz(sys.argv[2:],l.lista)
            l.wypisz(l.lista)
