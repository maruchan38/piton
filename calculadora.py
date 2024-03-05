print("**********************")
print("*    calculadora     *")
print("**********************\n")

print("----------------")
print("menu de opciones")
print("----------------\n")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. exponente")
print("5. division")
print("6. division entera")
print("7. modulo")

numero = int(input("selecciona la operacion a realizar :"))

if numero == 1:
    print("elegiste suma\n")
    numero = int(input("indica el primer numero :"))
    numero += int(input("indica el segundo numero :"))
    print("el resultado de la suma es :", numero )

elif numero == 2:
    print("elegiste resta\n")
    numero = int(input("indica el primer numero :"))
    numero -= int(input("indica el segundo numero :"))
    print("el resultado de la resta es :", numero )
    
elif numero == 3:
    print("elegiste multiplicacion\n")
    numero = int(input("indica el primer numero :"))
    numero *= int(input("indica el segundo numero :"))
    print("el resultado de la multiplicacion es :", numero )

elif numero == 4:
    print("elegiste exponente\n")
    numero = int(input("indica el primer numero :"))
    numero **= int(input("indica el segundo numero :"))
    print("el resultado de la expenonciacion(xd) es :", numero )

elif numero == 5:
    print("elegiste division\n")
    numero = float(input("indica el primer numero :"))
    numero /= float(input("indica el segundo numero :"))
    print("el resultado de la division es :", numero )

elif numero == 6:
    print("elegiste division entera\n")
    numero = int(input("indica el primer numero :"))
    numero //= int(input("indica el segundo numero :"))
    print("el resultado de la division entera es :", numero )

elif numero == 7:
    print("elegiste modulo\n")
    numero = int(input("indica el primer numero :"))
    numero %= int(input("indica el segundo numero :"))
    print("el resultado del modulo es :", numero )

else:
    print("operacion invalida o no registrada")




















    
