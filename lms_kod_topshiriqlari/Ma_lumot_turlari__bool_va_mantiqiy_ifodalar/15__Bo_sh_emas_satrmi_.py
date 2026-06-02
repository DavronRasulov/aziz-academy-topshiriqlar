import sys 

try:
    s = input()
    if s:
        print(True)
    else:
        print(False)
except EOFError:
    print(False)