#Calculadora
from math import cos, pi, sin, sqrt, tan


n1 = input("Escreva um número: ") 
op = input("Escreva uma operação, podendo ela ser(+, -, x, :, ^, media, /, cos, sen, tan): ")

if n1 == "pi" or n1 == "PI" or n1 == "Pi" or n1 == "pI":
    n1 = pi
else:
    n1 = float (n1) 
if op != "/" and op != "cos" and op != "sen" and op != "tan":
    n2 = input("Escreva um número: ")
    if n2 == "pi" or n2 == "PI" or n2 == "Pi" or n1 == "pI":
        n2 = pi
    else:
        n2 = float (n2)   
    if op == "+":
        soma = n1 + n2
        print(n1, "+", n2, "=", soma)
    elif op == "-":
        subt = n1 - n2
        print(n1, "-", n2, "=", subt)
    elif op == "x" or op == "X":
        mult = n1 * n2
        print(n1, "x", n2, "=", mult)
    elif op == ":":
        divi = n1 / n2
        print(n1, ":", n2, "=", divi)
    elif op == "^":
        pot = n1 ** n2
        print(n1, "^", n2, "=", pot)
    elif op == "media" or op == "MEDIA" or op == "Media" or op == "média" or op == "MÉDIA" or op == "Média":
        media = (n1 + n2) / 2
        print("A média entre", n1, "e", n2, "=", media)
elif op == "/" or op == "cos" or op == "sen" or op == "tan":
    if op == "/":
        raiz = sqrt(n1)
        print("/", n1, "=", raiz)
    elif op == "cos":
        cos = cos(n1)
        print("cos", n1, "=", cos)
    elif op == "sen":
        sen = sin(n1)
        print("sen", n1, "=", sen)
    elif op == "tan":
        tan = tan(n1)
        print("tan", n1, "=", tan)
