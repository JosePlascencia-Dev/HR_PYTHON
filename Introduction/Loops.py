"""
Problema:
The provided code stub reads an integer, `n`, from STDIN. For all non-negative integers i < n, print i^2.

Solucion: solucion propia.
"""

if __name__ == '__main__':
    n = int(input())
    # use range para hacer un for de tama;i exacto
    for i in range(n):
        print(i*i)