#variaveis
n1=0
n2=0
resultado=0

#função
def somar_numeros(num1,num2):
    resultado=num1+num2
    print(f"A soma dos numeros é: {resultado}")


#Algoritmo principal
n1= int(input("Informe um numero inteiro: "))
n2= int(input("Informe um numero inteiro: "))
somar_numeros(n1,n2)