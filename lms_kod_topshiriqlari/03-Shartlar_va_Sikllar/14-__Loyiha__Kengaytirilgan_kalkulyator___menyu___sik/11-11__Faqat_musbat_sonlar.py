a, b = map(int, input().split())
tanlov = int(input())

if a < 0 or b < 0:
    print("Invalid")
elif tanlov == 6:
    print(a ** b)