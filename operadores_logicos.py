#conjuncion

print("and")

num_1 = int(input("escribe un numero mayor a 2 y menor a 5:"))

if num_1 > 2 and num_1 < 5:
    print("el numero ", num_1, "cumple la concidion")
else:
    print("el numero ", num_1, "no cumple con la condicion ")

#disyuncion

palabra = input("para cumplir con la condicion escribe 'si' o 'yes'")

if palabra == "si" or palabra == "yes" :

    print("la condicion se cumplio")
else:
    print("la condicion no se ha cumplido")

#negacion

num_1 = int(input("escribe un numero igual a 5"))

if not num_1 == 5:
    print("el numero es diferente a 5 , y no cumple la condicion")
else :
    print("el numero es igual a 5 , y si cumple la condicion")
    



print(" fin ")
