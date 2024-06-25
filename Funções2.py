#variaveis
n1=0
n2=0
resultado=0

#função
def somar_numeros_com_retorno_3parametros(num1, num2):
    resultado=num1+num2
    return num1, num2 ,resultado


#Algoritmo principal

num1, num2, resultado = somar_numeros_com_retorno_3parametros(3,5)

print(f"O primeiro parametro foi: {n1}")
print(f"O segundo parametro foi: {n2}")
print(f"O resultado foi: {resultado}")