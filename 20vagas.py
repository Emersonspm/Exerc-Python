#variaveis
idade = 0
sexo = ""
mulheres = 0
idade_total = 0
idade_media = 0
maiores_idade = 0
contador = 0

#programa

for contador in range(0,20,1):
    sexo = input("Qual seu sexo? (M ou F)")
    idade = int(input("Qual sua idade? "))

    if (sexo.upper() == "F"):
        mulheres += 1

    if(idade >= 18):
        maiores_idade += 1

    idade_total += idade

idade_media = idade_total/20

print("A turma esta lotada")
print(f"A media das idades é: {idade_media}")
print(f"A quantidade de mulheres é: {mulheres}")
print(f"A quantidade de inscritos maiores de idade é: {maiores_idade}")