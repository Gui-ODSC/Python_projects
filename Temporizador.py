minu = int(input("Escreva os minutos: "))
seg = int(input("Escreva os segundos: "))


if minu > 60 or minu < 0 or seg < 0 or seg > 60:
    print("Tempo inválido")
else:
    seg = seg + 1
    while seg != 0:
        seg = seg - 1
        if seg == 0 and minu != 0:
            print(minu, "min  ", 0, "s")
            minu = minu - 1
            seg = 60
        else:
            print(minu, "min  ", seg, "seg")
       
if seg == 60:
    for i in range (seg, 0, -1):
        print(minu, "min  ", i, "s")
            
if minu == 0 and seg == 0 :
    print("Tempo Esgotado!!!")
