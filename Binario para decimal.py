#Dado um número binário inteiro e positivo, o sistema transforme em decimal
    #1º Passo = pedir o numero que será convertido!!!

bina = int(input("Escreva um número binário: "))

#Caso os algarismos digitados sejam diferentes de (0 e 1), avisar ao usuário!
#Declaração de variáveis
num = 0
pot = 0
cont1 = 0
soma = 0
deci = 0
cont2 = 0
ver = 0

for i in str(bina):
    num = int(i)
    cont1 = cont1 + 1
pot = 2 ** (cont1)
for i in str(bina):
    num = int(i)
    if pot != 0 and pot > 0:
        if num == 1:
            cont2 = cont2 + 1
            soma = pot//2
            pot = soma
            deci += pot
        elif num == 0:
            pot = pot // 2
for i in str(bina):
    num = int(i)
    if num != 1 and num != 0:
        ver = num
if ver != 0 and ver != 1:
    print(ver, "não é um dígito binário")
else:
    print(bina, "em decimal é",deci)
