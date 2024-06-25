#Variaveis
cont=0
vet=[0]*3

#Algoritmo
for cont in range(3):
    vet[cont] = int(input(f"Digite o {cont+1} numero: "))

for cont in range(3):
    print (vet[cont])

for cont in range(3):
    if (vet[cont]<0):
        print ("0")
    else:
        print ("1")
