#variaveis
mat1=[[0]*4,[0]*4,[0]*4]
linha=0
coluna=0

#Algoritmo

for linha in range (3):
    for coluna in range (3):
        mat1[linha][coluna] = int(input(f"Digite um numero para {linha}  {coluna}: "))

for linha in range (3):
    for coluna in range (3):
        print(f"[{mat1[linha][coluna]}]", end='')
    print()