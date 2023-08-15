N = int(input())

I = []
maior = 0

for i in range(0, N):
    I.append(int(input()))

d = 0
maior = 0
result = 0
c = 0
y = 1

while c != N:
    if(c == d):
        x = I[c]
       
        
    
    else:
        z = I[c]
        if(z != x):
            y += 1
            
        if((z == x) or (c == N - 1)):
            if(y >= maior):
                maior = y
                result = maior
            d += 1
            c = d
            y = 1
    
    c += 1
    
print(result)
            
            
            
    