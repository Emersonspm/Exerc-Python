#variaveis
mat=[[0]*3,[0]*3]
mat_trans=[[0]*2,[0]*2,[0]*2]
linha=0
coluna=0

#Algoritmo

for linha in range(2):
    for coluna in range(3):
        mat[linha][coluna] = int(input(f"Digite um numero para {linha} {coluna}: "))

print("___________Matriz original________")
for linha in range(2):
    for coluna in range(3):
        print (f"|{mat[linha][coluna]}|", end=' ')
    print()
print()

for linha in range(3):
    for coluna in range(2):
        mat_trans[linha][coluna] = mat[coluna][linha]

print("___________Matriz transposta________")
for linha in range(3):
    for coluna in range(2):
        print (f"|{mat_trans[linha][coluna]}|", end='')
    print()
print()
