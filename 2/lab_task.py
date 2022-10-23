import argparse
import re
import os.path

class NoFileError(Exception): #własny wyjątek dla braku pliku .txt
    pass

def convert(filename, leading_spaces, spaces):
    try:
        if os.path.isfile(filename):
            python = '\\'
            path= "/home/szymon/studies/sem3/ps/Script_Programming/2"
            file = open(path+"/"+filename,"r")
            print(f"{filename} succesfully opened")
            content = file.read().split('\n')
            print(content)
            #if spaces:
                #for e in content:
                    #e.split()
            pattern = re.compile('.*\\'+python+'$')
            #l_spaces = re.compile('^* ')
            new_content = ""
            for i in range(0,len(content)):
                if leading_spaces:
                    content[i] = re.sub(r'^\s+', '', content[i], flags=re.MULTILINE)
                if spaces:
                    content[i] = re.sub(r'\s+', '', content[i])
                if pattern.match(content[i]) != None:
                    new_content+=content[i][:-1]
                else:
                    if i != len(content)-1:
                        new_content+=content[i]+'\n'
                    else:
                        new_content+=content[i]
            file.close()
            file = open(path+"/"+filename+"1","w")
            file.write(new_content)
            file.close()
        else:
            print(f"{filename} does not exist")
    except PermissionError:
        print(f"{filename} cannot be opened")
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type = str, nargs="+", help='enter your file')
    parser.add_argument('--leading-spaces', help='use if you want to remove leading spaces', action = "store_true")
    parser.add_argument('--spaces', help='use if you want to remove duplicated spaces', action = "store_true")
    args = parser.parse_args()
    if args.leading_spaces:
        print("--leading-spaces turned on")
    if args.spaces:
        print("--spaces turned on")
    if args.c == None:
        print("Specify filename")
    else:
        for e in args.c:
            convert(e, args.leading_spaces, args.spaces)
