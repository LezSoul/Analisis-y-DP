print("Calcular los números primos dentro de un intervalo propuesto.")
x=int(input("Ingrese el número donde desea que el intervalo inicie: "))
y=int(input("Ingrese el número donde desea que el intervalo termine: "))

for numero in range (x, y):
    if numero > 1:
        cont=0
        i=2
        while i<numero and cont==0:
            resto=numero%i
            if resto==0:
                cont+=1
            i+=1
        if cont==0:
            print(numero)