def contador_dig(x):
    return len(str(x))


x = input("Digite uma frase: ")
resultado = contador_dig(x)
print(f"Quantidade de letras: {resultado}")