D = int(input())

D -= 3

while True:
    if (D >= 8):
        D = D // 8
        print(D)
        rest = D % 8
    else:
        break
    

if(rest == 3):
    sensor = 1
elif(rest == 4):
    sensor = 2
else:
    sensor = 3
