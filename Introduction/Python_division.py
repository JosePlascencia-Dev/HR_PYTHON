"""
Problema:
 The provided code stub reads two integers, `a` and `b`, from STDIN.
 Add logic to print two lines. The first line should contain the result of integer division, `a` // `b`  . The second line should contain the result of float division, `a`/`b`.
 No rounding or formatting is necessary.

Solucion: solucion propia.
"""
if __name__ == '__main__':
	a = int(input())
	b = int(input())
	# // para division entera
	print(a//b)
	# / para division flotante
	print(a/b)