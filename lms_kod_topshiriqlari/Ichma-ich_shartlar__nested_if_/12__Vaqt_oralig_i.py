hour = int(input())

if hour >= 0:
    if hour < 18:
        print("Day")
    else:
        print("Evening")
else:
    print("Night")