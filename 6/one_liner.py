import sys; from collections import Counter; print(dict(Counter(map(lambda c: len(c), sys.stdin.read().split()))))
