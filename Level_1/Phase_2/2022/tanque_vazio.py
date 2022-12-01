C = int(input())
D = int(input())
T = int(input())

if(T > D / C):
	result = 0 
else:
    result = D / C - T

print(f"{result:.1f}")