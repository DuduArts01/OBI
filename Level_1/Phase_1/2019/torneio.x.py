J1 = input(' ')
J2 = input(' ')
J3 = input(' ')
J4 = input(' ')
J5 = input(' ')
J6 = input(' ')

if(J1 == 'V'):
    V1 = 1
else:
    V1 = 0

if(J2 == 'V'):
    V2 = 1
else:
    V2 = 0

if(J3 == 'V'):
    V3 = 1
else:
    V3 = 0

if(J4 == 'V'):
    V4 = 1
else:
    V4 = 0

if(J5 == 'V'):
    V5 = 1
else:
    V5 = 0

if(J6 == 'V'):
    V6 = 1
else:
    V6 = 0

#cada participante disputou 6 jogos

v = V1 + V2 + V3 + V4 + V5 + V6
#Quantidade de vitórias

if(5 <= v <= 6):
    print(1)
    # participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
else:
    if(3 <= v <= 4):
            print(2)
        # participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
    else:
        if(1 <= v <= 2):
            print(3)
        # participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;
        else:
            print(-1)
# Se o participante não for colocado em nenhum dos três grupos seu programa deve imprimir o valor −1
#participantes que não venceram nenhum jogo não serão convidados a continuar com os treinamentos.

#V se o participante venceu o jogo, ou P se o jogador perdeu o jogo.
#Não há empates nos jogos
#Se o participante não for colocado em nenhum dos três grupos seu programa deve imprimir o valor −1

