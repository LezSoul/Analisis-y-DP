print("Calcula el factorial de un número")
num=int(input("Ingrese su número: "))
fact=1
i=1
while (i<=num):
    fact=fact*i
    i=i+1
print("El factorial de " + str(num) + " es "+str(fact))