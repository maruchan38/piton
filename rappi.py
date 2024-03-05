print("=======================================")
print("SISTEMA PARA DETERMINAR LOS DIAS LIBRES")
print("=======================================\n")

nombre =input("bienvenido al sistema para conocer tus dias de vacaciones , por favor ingrese su nombre :")

print(" un placer " , nombre )

clave = int(input( "a continuacion , escribe tu tipo de clave (solo el numero) : "))

tiempo = float(input("ahora , indica cuantos años has trabajado en la empresa :"))



if clave == 1:
    
    if tiempo == 1:
        print(nombre, "sus dias de vacaciones son :6 ")
        
    elif tiempo >= 2 and tiempo <= 6:
        print(nombre, "sus dias de vacaciones son :14")
        
    elif tiempo >= 7 :
        print(nombre, "sus dias de vacaciones son 20 ")


elif clave == 2:
    
    if tiempo == 1:
        print(nombre, "sus dias de vacaciones son :7 ")
        
    elif tiempo >= 2 and tiempo <= 6 :
        print(nombre, "sus dias de vacaciones son :15")
        
    elif tiempo >= 7:
        print(nombre, "sus dias de vacaciones son 22 ")


elif clave == 3:
    
    if tiempo == 1:
        print(nombre, "sus dias de vacaciones son :10 ")
        
    elif tiempo >= 2 and tiempo <= 6 :
        print(nombre, "sus dias de vacaciones son :20")
        
    elif tiempo >= 7 :
        print(nombre, "sus dias de vacaciones son 30 ")
        

else:
    print("la clave no existe o no esta determinada")


