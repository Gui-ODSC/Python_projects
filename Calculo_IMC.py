def indice_imc(peso, altura):
    return peso / (altura * altura)


def faixa(imc):
    if imc <= 16.9:
        f = "muito abaixo do peso"
    elif imc >= 17 and imc < 18.5:
        f =  "abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        f =  "peso normal"
    elif imc >= 25 and imc < 30:
        f =  "acima do peso"
    elif imc >= 30 and imc < 35:
        f =  "obesidade grau I"
    elif imac >=35 and imc <= 40:
        f =  "obesidade grau II"
    else:
        f =  "obesidade grau III"

    return f
    


p = float(input("digite o peso "))
a = float(input("digite altura "))

r = indice_imc(p, a)

print("IMC : ", r)
print(faixa(r))
