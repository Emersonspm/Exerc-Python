#variaveis
n = 0
menor = 0
maior = 0

#programa

n = int(input("Digite um numero inteiro (Digite 0 para sair): "))
menor = n
maior = n

while n != 0:
    if (n < menor) and (n != 0):
        menor = n
    if (n > maior):
        maior = n

    n = int(input("Digite um numero inteiro (Digite 0 para sair): "))

print(f"O maior numero é:  {maior}")
print(f"O menor numero é:  {menor}")
