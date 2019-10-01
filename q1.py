def segundo_grau(a,b,c):
	delta = (b * b) - (4 * a * c)

	if delta >= 0:
		raiz_1 = (-b + (delta ** (1/2))) / (2 * a)
		raiz_2 = (-b - (delta ** (1/2))) / (2 * a)

		print("x1=", raiz_1, "x2=", raiz_2)
		
		return 0

	parte_real = (-b) / (2 * a)
	x1_img = (-delta) ** (1/2) / (2 * a)
	x2_img = -(-delta) ** (1/2) / (2 * a)
	
	print("Parte real de x1 e x2:", parte_real)
	print("Parte imaginaria x1:", x1_img)
	print("Parte imaginaria x2:", x2_img)

	return 1

def main():
	a = int(input())
	b = int(input())
	c = int(input())

	resultado = segundo_grau(a, b, c)

	print(resultado)

main()