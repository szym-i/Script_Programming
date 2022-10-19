import argparse
import re
import os.path

class NoFileError(Exception): #własny wyjątek dla braku pliku .txt
    pass

def print_l(file):
    try:
        if os.path.isfile(file):
            path= "/home/szymon/studies/sem3/ps/Script_Programming/2"
            opened_file = open(path+"/"+file,"r")
            print(f"{file} succesfully opened")
            file = opened_file.readlines()
            print(file)
            for line in file:
                x = re.split('/+',line)
                print(x)
            opened_file.close()
        else:
            print(f"{file} does not exist")
    except:
        print("{file} is not file")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type = str, nargs="+", help='enter your file')
    args = parser.parse_args()
    for e in args.c:
        print_l(e)
