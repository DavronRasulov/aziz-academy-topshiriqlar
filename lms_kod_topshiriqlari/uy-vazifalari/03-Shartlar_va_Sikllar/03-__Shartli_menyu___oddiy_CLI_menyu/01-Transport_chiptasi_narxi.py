transport = int(input())
toifa = int(input())

if transport == 1:
    narx = 1700
elif transport == 2:
    narx = 1700 
elif transport == 3: 
    narx = 4000 
else:
    print("Notogri transport")
    narx = None 
    
if narx is not None:
    if toifa == 1:
        yakuniy = narx 
    elif toifa == 2:
        yakuniy = narx // 2
    elif toifa == 3:
        yakuniy = 0
    else:
        print("Notogri toifa")
        yakuniy = None 
        
    if yakuniy is not None:
        print(yakuniy)