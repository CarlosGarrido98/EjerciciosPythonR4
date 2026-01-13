
#Importamos el paquete operaciones
import operaciones as op 


#Pruebas Ejercicio 1

#Prueba funcion info_argumentos
print(op.info_argumentos(1,2,3))
#print()

#Prueba funcion divisibles3
print(op.divisibles3(3,5,9))
#print()

#Prueba funcion histograma 
op.histograma(4,9,7)


#Prueba Ejercicio 2 

#Caso de prueba si se quiere enviar un paquete de un kilo que NO es urgente
print("El coste final del envio sería:" , op.coste_envio(1))
#Caso de prueba si se quiere enviar un paquete de un kilo que SI es urgente 
print("El coste final del envio sería:" , op.coste_envio(1,True))



print()
#Prueba Ejercicio 3


try:

    horas = int(input("Introduce las horas:"))
    minutos = int(input("Introduce los minutos:"))
    segundos = int(input("Introduce los segundos:"))


    
    if horas <0 or horas >23 :
        raise ValueError("Esa hora no es válida")

    if minutos <0 or minutos>59:
        raise ValueError("Esos minutos no son válidos")

    if segundos <0 or segundos>59:
        raise ValueError("Esos segundos no son válidos")

    print("Total en segundos: ", op.convertir_segundos(horas,minutos,segundos))

except ValueError as e :
        print("Error:", e )

    