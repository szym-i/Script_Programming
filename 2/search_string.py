import re

if __name__ == "__main__":
    while True:
        try:
            input_list = input().split()
            for x in input_list:
                numbers = re.findall('[0-9]+', x)
                words = re.findall('[A-z]+', x)
                if words != []:
                    print(f"Words: {words}")
                if numbers != []:
                    print(f"Numbers: {numbers}")
        except:
            quit()
