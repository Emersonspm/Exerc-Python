# variaveis
mat = [
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5,
]
linha = 0
coluna = 0

# Algoritmo

for linha in range(0, 4, 1):
    for coluna in range(0, 4, 1):
        mat[linha][coluna] = int(input(f"Digite um numero para {linha} {coluna}: "))

for linha in range(0, 4, 1):
    for coluna in range(0, 4, 1):
        if linha == coluna:
            print(f"[{mat[linha] [coluna]}]", end="")
