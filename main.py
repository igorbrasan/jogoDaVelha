from array import array
def verificarLinhas():
    for i in range (3):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2]:
            print("fim de jogo!")

print ('hello');

tabuleiro = [['e','f','c'],
             ['d','s','a'],
             ['b','b','b']]
print(tabuleiro[0])
print(tabuleiro[1])
print(tabuleiro[2])
verificarLinhas()