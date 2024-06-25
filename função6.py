def valor_pagam():
    diario = []
    while True:  # 'True' deve começar com letra maiúscula 'T'
        v = float(input("Valor da prestação: "))
        a = int(input("Dias atrasados: "))
        if a > 0:
            m = 0.03
            d = 0.001 * a         
            total = float(v + (v * d) + (v * m))
        else:
            total = v

        print(f"O valor a ser pago é R${total} ")
        diario.append(total)

        continuar = input("Continuar? S/N: ").upper()
        if continuar == 'N':
            break

valor_pagam()