## Problema:

> Given an integer, `n`, perform the following conditional actions:
> 
> - If `n` is odd, print `Weird`
> - If `n` is even and in the inclusive range of to- , print Not Weird
> - If `n` is even and in the inclusive range of to- , print `Weird`
> - If `n` is even and greater than , print `Not Weird`
## Solución: Solución propia.
### Código de la solución
```
import math
import os
import random
import re
import sys

if __name__ == '__main__':
	n = int(input().strip())
	if n%2 == 0:
		if n >= 2 and n <= 5:
			print("Not Weird")
		elif n >= 6 and n <= 20:
			print("Weird")
		elif n > 20:
			print("Not Weird")
	else:
		print("Weird")
``` 
### Explicación de la respuesta

Primero se determina si el numero es par o no, si es par se aplican las condiciones para evaluar los números de menor a mayor.