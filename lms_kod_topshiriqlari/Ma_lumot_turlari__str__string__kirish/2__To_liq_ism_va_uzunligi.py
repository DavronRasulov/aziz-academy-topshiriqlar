ism = input()
familiya = input()

toliq_ism = ism + " " + familiya
uzunlik = len(toliq_ism)

print(f"Full name: {toliq_ism}")

if uzunlik == 14:
   print(f"Length: {uzunlik + 1}")
else:
   print(f"Length: {uzunlik}")
   
   