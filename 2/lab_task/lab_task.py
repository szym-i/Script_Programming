import argparse
import re
import os.path

def convert(content, leading_spaces, spaces, c):
    pattern = re.compile('.*\\'+c+'$')
    new_content = ""
    for i in range(0,len(content)):
        l_s = 0
        for j in content[i]:
            if j == ' ':
                l_s+=1
        if spaces and leading_spaces:
            content[i] = re.sub(r'\s+', '', content[i])   
        if spaces and not leading_spaces:
            content[i] = l_s*' '+re.sub(r'\s+', '', content[i])       
        if leading_spaces:
            content[i] = re.sub(r'^\s+', '', content[i], flags=re.MULTILINE) #flaga sprawia że ^ działa na początku każdej linii a nie tylko tekstu   
        if pattern.match(content[i]) != None:
            new_content+=content[i][:-1]
        else:
            if i != len(content)-1:
                new_content+=content[i]+'\n'
            else:
                new_content+=content[i]
    print(f"Output:\n{new_content}",end="")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', help = "enter files", nargs="+")
    parser.add_argument('-c',type=str, help='enter your file', nargs=1, required=False, default = '\\')
    parser.add_argument('--leading-spaces', help='use if you want to remove leading spaces', action = "store_true", required=False)
    parser.add_argument('--spaces', help='use if you want to remove duplicated spaces', action = "store_true", required=False)
    args = parser.parse_args()
    print(args)
    c = args.c[0]
    print(f"-c = '{c}' (default:'\\')")
    print(f"--leading-spaces: {args.leading_spaces}")
    print(f"--spaces: {args.spaces}")
    if args.filenames == None:
        print("Convert input mode (press Ctrl+D to stop)")
        content = ""
        try:
            while True:
                user = input()
                content+=(user+'\n')
        except EOFError:
            print("Converted output:")
            content = content[:-1].split('\n')
            print(content)
            convert(content, args.leading_spaces, args.spaces, c)
    else:
        for filename in args.filenames:
            try:
                if os.path.isfile(filename):
                    file = open(filename,"r")
                    print(f"File {filename} succesfully opened")
                    content = file.read().split('\n')
                    file.close()
                    convert(content, args.leading_spaces, args.spaces, c)
                else:
                    print(f"File {filename} does not exist")
            except PermissionError:
                print(f"File {filename} cannot be opened (Permission Error)")

