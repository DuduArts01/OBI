N = int(input())

for i in range(0, N):
    n = input()
    V = int(input())
    if(i == 0):
        Vmax = V
        Nmax = n
    elif(Vmax < V):
        Vmax = V
        Nmax = n

print(Nmax)
print(Vmax)