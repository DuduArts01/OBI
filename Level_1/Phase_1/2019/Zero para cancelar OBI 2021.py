Rf = int(input())
#Quantas vezes repete a fala
NA = int(input())
#na é o número anterior
Rf = Rf - 1
#Subtrai o Rf antes porque já comecei colocando um valor no 'na' antes da repetição
Nf = NA
# por ter inserido o valor antes da repetição
#Nf é número falado
while Rf > 0:
    Rf = Rf - 1
    n = int(input())
    #n é o número que irá falar
    if(n == 0):
       N = Nf - NA
       # N é número
    else:
        N = Nf + n
    NA = n
    #nf número final
    print (nf)
    if f == 0:
        break

