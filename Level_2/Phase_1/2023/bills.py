V = int(input())
A = int(input())
F = int(input())
P = int(input())

c = 0

if(V >= A):
    V -= A
    c += 1
if(V >= F):
    V -= F
    c += 1
if(V >= P):
    V -= P
    c += 1
    
print(c)