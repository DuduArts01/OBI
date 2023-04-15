numeros = int(input())
result = 0;
for i in range(numeros):
    x = str(input())
    result += int(x[:-1])**int(x[-1])
print(result)
   
  
