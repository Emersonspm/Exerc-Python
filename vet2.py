#variaveis
vet=[0.0]*50
cont=0

#Algoritmo
for cont in range(50):
    vet[cont]=int(input(f"Digite o {cont+1} numero: "))
    if( cont % 2 == 0):
        vet[cont]= vet[cont]*1.02
    else:
        vet[cont]= vet[cont]*1.05

for cont in range(50):
    print(f"{vet[cont]:.2f}", end='  ')
