import sys

if __name__ == '__main__':
    odd = 0
    for i in range(1,len(sys.argv)):
        try:
            file = open(sys.argv[i], "r")
            number = ""
            a = file.read().split()
            for number in a:
                if int(number) % 2 == 0:
                    odd += 1
            file.close()
        except FileNotFoundError:
            print(f'file {sys.argv[i]} does not exist')
        except ValueError:
            pass
        except PermissionError:
            print(f'file {sys.argv[i]} can not be opened')
    print(f'There are {odd} odd numbers in entered files') 
