opcion = 0
while True:
    print("""
    Menú
    
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Regresar al menu
    6) Salir
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print(" La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print(" La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print(" El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        if n2 != 0:
            print(" ")
            print(" La division de",n1,"/",n2,"es igual a",n1/n2)  
        else: 
            print('El numero es indefinido') 
    elif opcion == 5:
        opcion = 0
    elif opcion == 6:
        break
    else:
        print("Opción incorrecta")