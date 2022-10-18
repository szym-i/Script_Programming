import getopt
import sys


if __name__ == '__main__':
    short = "m:"
    long = ["module="]
    if len(sys.argv) < 2:
        print("Use --module=")
        quit()
    oplist, args = getopt.getopt(sys.argv[1:], short, long)
    print(f"oplist={oplist}, args={args}")
    match oplist[0][1]:
        case "slownik":
            import slownik as s
            s.wypisz(s.slownik)
            s.zapisz(args,s.slownik)
            s.wypisz(s.slownik)
        case "lista": 
            import lista as l
            l.wypisz(l.lista)
            l.zapisz(args,l.lista)
            l.wypisz(l.lista)
        case _:
            print("Try --module=slownik/lista")
