"""
Problema:
The included code stub will read an integer, `n` , from STDIN.
Without using any string methods, try to print the following:
123 . . .n
Note that ". . ." represents the consecutive values in between.

Solucion: solucion propia
"""
#cree esta funcion que toma como argumento el numero y que concatena el valor de la iteracion mas uno (dado que los rangos empiezan en 0) para imprimir el mensaje esperado.
def noseXD(n):
    cad = ""
    for i in range(n):
        cad += str(i+1)
    print(cad)
    
if __name__ == '__main__':
    n = int(input())
    noseXD(n)