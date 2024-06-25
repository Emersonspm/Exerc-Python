lista =[0]*5
for c in range (0,5,1):
    lista[c]=int(input("Digite um numero: "))

soma=0   
for c in range (0,5,1):
    soma += lista[c]

media = soma/5
print(f"A média dos valores é: {media}")

distanciaA=1
distanciaF=1

for c in range (0,5,1):
    abs(lista[c]-media) = distanciaA
        if distanciaA < distanciaF:
            distanciaF = distanciaA

print (f"numero mais proximo da media é: {distancia}")
