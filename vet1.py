#Variaveis
contador=0
vetor=[0]*6
diferença=0

#Algoritmo
for contador in range(0,6,1):
    vetor[contador]=int(input(f"Digite um numero {contador+1}: "))

for contador in range(0,6,1):
    if vetor[contador]<0:
        print (vetor[contador]*-1)
    elif (vetor[contador]>=10):
        diferença = int(input(f"Digite um numero para a diferença "))
        print (vetor[contador]-diferença)

    else:
        print (vetor[contador]/5)