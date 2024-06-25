#variaveis
idade = 0
contador = 0
n = 0
idade_media = 0
idade_soma = 0
idade_maior = 0
idade_menor = 0

#programaidade

n = int(input("Digite a quantidade de pessoas "))

for contador in range (0,n,1):
    idade = int(input(f"Informe a idade: "))

    if (contador == 0):
        idade_maior = idade
        idade_menor = idade
    else:
        if(idade > idade_maior):
            idade_maior = idade
        if(idade < idade_menor):
            idade_menor = idade

    idade_soma += idade

    idade_media = idade_soma / n

print(f" A idade media é: {idade_media:.2f}")
print(f" A idade maior é: {idade_maior}")
print(f" A idade menor é: {idade_menor}")