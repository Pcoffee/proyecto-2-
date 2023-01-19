def generar_matriz(numero): 
    matriz_vacia = []
    matriz_final = []
    for n in range(numero):
        matriz_vacia.append([])
        matriz_final.append([])
    asignar_numero = 0
    for m1 in range(numero):
        for m2 in range(numero):
            asignar_numero = asignar_numero + 1
            matriz_vacia[m1].append(asignar_numero)
    
    contador_par = 0
    contador_impar =0
    for i in range (numero):
        if i % 2 == 0:
            contador_par = contador_par + 1
        if i % 2 != 0:
            contador_impar = contador_impar + 1
    inicio=0
    for par in range(contador_par):
        matriz_final[par] = matriz_vacia[inicio]
        inicio = inicio + 2
    final=numero-1
    for impar in range (contador_impar):
        matriz_final[contador_par+impar] = matriz_vacia[final]
        final = final -2
    print(matriz_final)
    
generar_matriz(6)

numero = input("ingrese el grado de la matriz")
    
