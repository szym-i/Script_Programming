import sys

print(len(list(filter(lambda c: int(c) % 2 == 0, sum(list(map(lambda x: open(x, 'r').read().split(), sys.argv[1:])), [])))))
