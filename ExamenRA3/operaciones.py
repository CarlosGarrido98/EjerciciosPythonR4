

#1ºFuncion Ejercicio1
def info_argumentos(*args):

    cont = 0 
    for i in args:
        cont +=1

    return cont 

#2ºFuncion Ejercicio1
def divisibles3(*args):

    numeros = []

    for i in args:
       if i % 3 == 0 :
          numeros.append(i)

    return numeros     

#3ºFuncion Ejercicio1
def histograma(*args):

     for i in args:
        print (i * "*")


#1º Funcion Ejercicio2

def coste_envio( kilos , urgente = False , tarifa_base = 5  ):

    kilosfinales = kilos * 2

    #Correcion en el * 
    tarifa_final = tarifa_base + kilosfinales 

    #Redundacion con true
    if urgente: 

        incremento = (tarifa_final * 30  ) /100

        tarifa_final = tarifa_final + incremento

    return tarifa_final 




#1 Funcion Ejercicio3 


def convertir_segundos(horas,minutos,segundos):


    #La operacion del programa 
    horasenSegundos = (horas * 60 ) * 60 

    minutosenSegundos = minutos * 60 

    totalenSegundos = horasenSegundos + minutosenSegundos + segundos 

    return totalenSegundos
    

