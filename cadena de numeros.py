#Cadena de Numeros

def mi_funcion (numero):
    i=0
    lista = []
    numeroString = str(numero)
    while numeroString != "89" and numeroString != "1" :
        i = i+1
        numeroSuma = 0
        for n in numeroString:
            numeroSuma = numeroSuma + int(n)**2
            numeroString=str(numeroSuma)
        lista.append(numeroSuma)
    return lista.pop() if lista else 0
    
def encontrar_porcentaje (numero):
     contador = 0
     for n in range(numero):
         numero_cadena = mi_funcion(n + 1)
         if numero_cadena == 89:
             contador += 1
     resultado = contador / numero * 100
     print("El porcentaje de los numeros que dio como resultado 89 es : ", resultado, "y el porcentaje de los numeros que dio como resultado 1 es : ", 100-resultado)
             
variable= int( input( " introduce el numero a calcular : ") )

encontrar_porcentaje(variable)