#el calculo de pi

def serie_seno(m):
    sumatoria =0
    for n in range(m):
        sumatoria += (-1)**(n)*(1/(n+1)**6)
    pi = ((30240 * sumatoria)/31)**(1/6)
    print(pi)
        
numero= int(input( "ingrese  el numero :"))
serie_seno(numero)
    