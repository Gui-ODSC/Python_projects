from itertools import chain
lista = []
lista1 = []
soma = 0
cont = 0
n = int(input("Escreva um número e dê enter: "))
if n >= 0 and n <= 10:
    lista.append(n)
    while n >= 0 and n <= 10:
        n = int(input("Escreva um número e dê enter: "))
        if n >= 0 and n <= 10:
            lista.append(n)
    for item in chain(lista):
        cont += 1
        print(cont)
        if item not in lista1:
            lista1.append(item)
            soma += item
    print(soma)
        



            
    #for i in range(0, len(lista)):
        #print(lista[0])
        #for j in range(0, len(lista)):
            #if lista[i] != lista[j]:
                #print(lista[j])
    
    #print(max(lista))
    #print(min(lista))
    #print(guarda)

