#variaveis
c9=0
c12=0
c23=0
c40=0
canal=0
outrosc=0
p9=0
p12=0
p23=0
p40=0
poutros=0
porcentagem=0

#programa
canal=1
while (canal!=0):
    canal=int(input("Informe um canal (9|12|23|40) Digite 0 para sair: "))

    if(canal == 9):
        porcentagem += 1
        c9 += 1
    else:
        if(canal == 12):
            porcentagem += 1
            c12 += 12 
        else:
            if(canal == 23):
                porcentagem += 1
                c23 += 23
            else:
                if(canal == 40):
                    porcentagem += 1
                    c40 += 40
                else:
                    if(canal !=0):
                        outrosc += 1
                        porcentagem += 1 
       
       
if (porcentagem > 0):
    p9 = (c9 * 100) / porcentagem
    p12 = (c12 * 100) / porcentagem
    p23 = (c23 * 100) / porcentagem
    p40 = (c40 * 100) / porcentagem
    poutros = (outrosc * 100)/ porcentagem

print (f" A porcentagem do canal 9 é: {p9:,.2f} %")
print (f" A porcentagem do canal 12 é: {p12:,.2f}%")
print (f" A porcentagem do canal 23 é: {p23:,.2f}%")
print (f" A porcentagem do canal 40 é: {p40:,.2f}%")
print (f" A porcentagem de outros canais é: {poutros:,.2f}%")