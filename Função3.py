#Variaveis

#Função

def soma_multi(n1,n2,n3):
    return n1+ n2+ n3, n1* n2* n3

#Algoritimo

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

soma, multi = soma_multi(n1,n2,n3)
print(soma)
print(multi)