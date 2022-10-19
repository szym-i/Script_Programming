import re

if __name__ == "__main__":
    words = re.compile("[A-z-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+")
    numbers = re.compile("[0-9]+")
    while True:
        try:
            input_list = input().split()
            for w in input_list:
                splitted = re.split('(\d+)',w)
                for e in splitted:
                    word = words.match(e) # jeśli nie matchuje do patternu czyli nie jest słowem przyjmie wartość None
                    number = numbers.match(e) # to samo tylko z liczbą
                    match word:
                        case None:
                            pass
                        case _:
                            print(f"word: {e}")
                    match number:
                        case None:
                            pass
                        case _:
                            print(f"number: {e}")
        except EOFError:
            quit()
        except KeyboardInterrupt:
            quit()
