#Ejercicio 1
#Dadas las funciones ExVar1(), ExVar2(), y ExVar3(), calcular el resultado de ejecutar cada función considerando el alcanze de sus variables.
#Nota: Las funciones son ejecutadas en orden

x, y = 5, 2

def ExVar1():
    print(x,y)
    
def ExVar2():
    x = 2
    def ExVar21():
        nonlocal x
        y, x = x, y
        print(x,y)
    ExVar21()
    
def ExVar3():   
    def ExVar31():
        global x, y
        x, y = y, x
    ExVar31()    
    print(x,y)

