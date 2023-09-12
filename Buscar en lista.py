list = [5, 10, 55, 66, 88, 26, 19, 18, 30, 569, 785, 222, 333, 568, 0, 3, 7, 52, 11, 90, 106, 12345, 1003, 1000, 8, 39856, 77,] 
print("Buscar un elemento dentro de la lista.")
print (list)

numero = int(input("Ingrese el número a buscar: "))

if numero in list:
    print("El número", numero, "SI se encuentra en la lista.")
else: 
    print ("El número", numero,  "NO se encuentra en la lista.")