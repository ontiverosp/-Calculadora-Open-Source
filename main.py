from sumar import sumar
from resta import resta
from multplicacion import multplicacion
from dividir import dividir
from suma_avanzada import suma_avanzada

flag = 0
while flag != 6:
    print("\nSeleciona que quieres hacer \n 1. Sumar 2 numeros \n 2. Restar 2 numeros \n 3. Multiplicar 2 numeros \n 4. Dividir 2 numeros \n 5. Sumar mas de 2 numeros \n 6. Salir")
    flag =  int(input("Seleccion: "))
    if flag == 1:
        num1 = int(input("Dame el primer sumando: "))
        num2 = int(input("Dame el segundo sumando: "))
        print("La suma es: " + str(sumar(num1,num2)))
    elif flag == 2:
        num1 = int(input("Dame el minuendo: "))
        num2 = int(input("Dame el sustraendo: "))
        print("La resta es: " + str(resta(num1,num2)))
    elif flag == 3:
        num1 = int(input("Dame el primer factor: "))
        num2 = int(input("Dame el segundo factor: "))
        print("El producto es: " + str(multplicacion(num1,num2)))
    elif flag == 4:
        num1 = int(input("Dame el dividendo: "))
        num2 = int(input("Dame el divisor: "))
        print("El cociente es: " + str(dividir(num1,num2)))
    elif flag == 5:
        nums = input("dame los sumandos separados por una coma: ").split(",")
        nums_int = [eval(i) for i in nums]
        print("La suma es: " + str(suma_avanzada(nums_int)))
    elif flag == 6:
        break
    else:
        print("\nNo fue una de las opciones!\n")
    

    