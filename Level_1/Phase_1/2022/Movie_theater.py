#Two friends are in queue

#

#Given the ages of the friends, write a program to calculate the total to be paid for the two tickets

i1 = int(input())

i2 = int(input())

#Entrada: A entrada contém duas linhas, cada linha contendo um inteiro, a idade de uma das amigas.

if (i1 <= 17 ):

    p1 = 15

else:

    if (18 <= i1 <= 59):

        p1 = 30

    else:

        if(i1 >= 60):

          p1 = 20

if (i2 <= 17 ):

    #até 17 anos

    p2 = 15

else:

    if (18 <= i2 <= 59):

        #18 a 59 anos 

        p2 = 30

    else:

        if(i2 >= 60):

          	#60 anos ou mais           p2 = 20

Sp = p1 + p2

print(Sp)
