CP = {}
'''Dictionary from number of chocolates and prices '''

N = int(input())
'''N is number of chocolate'''

pricetotal = 0
'''Price total'''

for i in range(1, N + 1):
    CP[i] = int(input()) 
    '''Add the price'''
    pricetotal += CP[i]
    if(i % 3 == 0):
        menor = 999
        for c in range(i, i - 3, -1):
            if(CP[c] < menor):
                menor = CP[c]
        pricetotal -= menor
print(pricetotal)
