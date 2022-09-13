import re

if __name__ == "__main__":
    while True:
        try:
            str = input()
            numbers = re.findall('[0-9]+', str)
            words = re.findall('[a-z]+',str)
            if words != None:
                print(f"Words: {words}")
            if numbers != None:
                print(f"Numbers: {numbers}")
        except:
            quit()
