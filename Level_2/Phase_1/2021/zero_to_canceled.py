Nlist = list()
N = int(input())

def zero(n):
    Nlist.pop()

for i in range(0, N):
    Xi = int(input())
    if(Xi == 0):
        zero(Xi)
    else:
        Nlist.append(Xi)
print(sum(Nlist))
