#Ejercicio 5
#Ejercicio 4
#Implementar una función recursiva que calcule la suma de 
#una lista de números enteros.

def suma_lista_rec(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_lista_rec(lista[1:])
numeros=[1,2,3,4,5]
print(suma_lista_rec(numeros))