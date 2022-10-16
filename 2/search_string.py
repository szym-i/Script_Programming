import re

if __name__ == "__main__":
    while True:
        words = re.compile("[A-z]+")
        numbers = re.compile("[0-9]+")
        try:
            input_list = input().split()
            for w in input_list:
                a = re.split('(\d+)',w)
                for e in a:
                    word = words.match(e)
                    number = numbers.match(e)
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
        except:
            quit()
