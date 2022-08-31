
lista1 = []
elemento = int(input("Escreva um elemento da lista: "))
lista1.append(elemento)
while elemento >= 0:
    elemento = int(input("Escreva um elemento da lista: "))
    if elemento >= 0:
        lista1.append(elemento)
for i in range(0, len(lista1)):
    print(i, lista1[i])  
lista2 = []
n1 = int(input("Escreva um índice da lista: "))
n2 = int(input("Escreva outro elemento da lista: "))

for i in range(0, n1):
    lista2.append(lista1[i])
    print(i, lista2[i])
    
for i in range(n1, n2):
    guarda = lista1[n1]
    lista2.append(lista1[i+1])
    print(i, lista2[i])
    
lista1[n2] = lista1[n1]
lista2.append(lista1[n2])
print(n2, lista2[n2])

for i in range((n2+1) , len(lista1)):
    lista2.append(lista1[i])
    print(i, lista2[i])

    
