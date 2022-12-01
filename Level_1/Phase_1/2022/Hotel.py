#Entrada:
D = int(input())
    #A primeira linha contém um inteiro D, o valor da diária no dia 1.
A = int(input())
#A segunda linha contém um inteiro A, o aumento da diária a cada dia a partir do dia 2 até o dia 15 (inclusive).
N = int(input())
#  A terceira linha contém um inteiro N, o dia de chegada no hotel

if(N == 1):
    Vt = 31 * D
    # • Quem chegar no dia 1 vai pagar um total de 31 × D Reais.
    
if (N == 2):
    V = D + A            
    d = 31 - N + 1
    Vt = d * V
    #a diária é D + A Reais para quem chegar no dia 2;
            
if (N == 3):
    V = D + 2 * A
    #D + 2 × A Reais no dia 3;
    d = 31 - N + 1
    Vt = d * V
                   
if (N == 4):
    V = D + 3 * A
    # D + 3 × A Reais no dia 4 e assim por diante.
    d = 31 - N + 1
    Vt = d * V
                            
if (N == 5):
    V = D + 4 * A
    d = 31 - N + 1
    Vt = d * V
                                    
if (N == 6):
    V = D + 5 * A
    d = 31 - N + 1
    Vt = d * V
                                            
if (N == 7):
    V = D + 6 * A
    d = 31 - N + 1
    Vt = d * V
                                                    
if (N == 8):
    V = D + 7 * A
    d = 31 - N + 1
    Vt = d * V
                                                            
if (N == 9):
    V = D + 8 * A
    d = 31 - N + 1
    Vt = d * V
                                                                    
if (N == 10):
    V = D + 9 * A
    d = 31 - N + 1
    Vt = d * V
                                                                            
if (N == 11):
    V = D + 10 * A
    d = 31 - N + 1
    Vt = d * V
                                                                                    
if (N == 12):
    V = D + 11 * A
    d = 31 - N + 1
    Vt = d * V
                                                                                            
if (N == 13):
    V = D + 12 * A
    d = 31 - N + 1
    Vt = d * V
                                                                                                    
if (N == 14):
    V = D + 13 * A
    d = 31 - N + 1
    Vt = d * V                                          
                                                                                                            
if (N == 15):
    V = D + 14 * A
    d = 31 - N + 1
    Vt = d * V
                                                                                                                    
if (N >= 16):
    V = D + 14 * A
    d = 31 - N + 1
    Vt = d * V
    # • A partir do dia 16 a diária não aumenta mais.
print(Vt)