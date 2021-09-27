n1 = int(input("Introduce tu primero número: ") )
n2 = int(input("Introduce tu segundo número:" ) )

opcion = 0
while True:
    print("""
    Dime, ¿Qué operación quieres hacer?

    1) Sumar los dos números.
    2) Restar los dos números.
    3) Multupplicar los dos números.
    4) Cambiar los dos números elegidos.
    5) Salir de la calculadora.
    """)

    opcion = int(input("Elige una opción: ") )
    
    if opcion == 1:
        print (" ") 
        print("RESULTADO: La suma de ",n1, "+",n2, "es igual  a" ,n1+n2)
    elif opcion == 2:
            print (" ")
            print("RESULTADO: La resta de ",n1 ,"-",n2, "es igual a" ,n1-n2)
    elif opcion == 3:
                print(" ")
                print("RESULTADO: La Multiplicación de ",n1 ,"*",n2, "es igual a" ,n1*n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 5:
        break
    else:
        print("Opción Incorrecta")