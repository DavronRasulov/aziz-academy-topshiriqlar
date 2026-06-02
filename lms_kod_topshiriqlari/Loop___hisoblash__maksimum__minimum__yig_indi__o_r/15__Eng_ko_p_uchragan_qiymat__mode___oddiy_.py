n = int(input())
sonlar = list(map(int, input().split()))

eng_kop_ucragan = sonlar[0]
max_count = 0 

for x in sonlar:
    hozirgi_count = sonlar.count(x)
    
    if hozirgi_count > max_count:
        max_count = hozirgi_count
        eng_kop_uchragan = x
        
    elif hozirgi_count == max_count:
        if x < eng_kop_uchragan:
            eng_kop_uchragan = x
            
print(eng_kop_uchragan)