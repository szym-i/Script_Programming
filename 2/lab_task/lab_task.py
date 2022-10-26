import argparse
import re
import os.path

def convert(content, leading_spaces, spaces, c):
    pattern = '\\'+c+r'\n'
    content = re.sub(pattern,'',content)
    if spaces and leading_spaces: # --spaces --leading-spaces
        tmp_content=""
        for line in content.split('\n'):
            line = re.sub(r'\s+', '', line) 
            tmp_content+=(line+'\n')
        content = tmp_content[:-1] # pozbywamy się \n z końca
    elif spaces: # --spaces
        tmp_content=""
        for line in content.split('\n'):
            l_s = 0 # number of leading spaces
            for c in line:
                if c == ' ':
                    l_s+=1
                else:
                    break
            line = re.sub(r'\s+', '', line) 
            tmp_content+=(l_s*' '+line+'\n')# add leading spaces back
        content = tmp_content[:-1] # remove additional \n
    elif leading_spaces: # --leading spaces
        content = re.sub(r'^\s+', '', content)         
    print(f"Output:\n{content}",end="")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "enter files", nargs="*")
    parser.add_argument('-c',type=str, help='enter line continuation character', nargs=1, required=False, default = '\\')
    parser.add_argument('--leading-spaces', help='use if you want to remove leading spaces', action = "store_true")
    parser.add_argument('--spaces', help='use if you want to remove whitespaces', action = "store_true")
    args = parser.parse_args()
    c = args.c[0]
    print(f"-c = '{c}' (default = '\\')")
    print(f"--leading-spaces: {args.leading_spaces}")
    print(f"--spaces: {args.spaces}")
    if args.file == []:
        print("Convert input mode (press Ctrl+D to stop)")
        content = ""
        try:
            while True:
                user = input()
                content+=(user+'\n')
        except EOFError:
            print("Converted output:")
            convert(content[:-1], args.leading_spaces, args.spaces, c)
    else:
        for filename in args.file:
            try:
                if os.path.isfile(filename):
                    file = open(filename,"r")
                    print(f"File {filename} succesfully opened")
                    content = file.read()#.split('\n')
                    file.close()
                    convert(content, args.leading_spaces, args.spaces, c)
                else:
                    print(f"File {filename} does not exist")
            except PermissionError:
                print(f"File {filename} cannot be opened (Permission Error)")

