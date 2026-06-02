yashirin_son = 10
max_urinishlar = 5
topildi = False

for i in range(max_urinishlar):
    son = int(input())
    
    if son == yashirin_son:
        print("Correct")
        topildi = True
        break

if not topildi:
    print("You lost")
            
    