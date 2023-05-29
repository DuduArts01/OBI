N = int(input())
K = int(input())

number = []

x = 0
#x is amount of sum rectangle

c = 0
#c is the sum of values

for i in range(0, N):
    number.append(int(input()))
    # get value
    
    c += number[i]
    
    if(c > K):
        c = number[i]
    if(c == K):
        x += 1
    

print(f"x = {x}\n")