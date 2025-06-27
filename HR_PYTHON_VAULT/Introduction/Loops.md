## Problema:

> The provided code stub reads an integer, `n`, from STDIN. For all non-negative integers $i < n$, print $i^2$.
## Solución: Solución propia.
### Código de la solución
```
if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		print(i*i)
``` 
### Explicación de la respuesta
se uso `range` para determinar el numero de iteraciones que se deben realizar, dentro del loop solo se imprimió `i*i`.