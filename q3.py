def Pi():
	valor_pi = 1
	cont = 0
	divisor = 3

	while True:
		valor_teste = 0
		comparar = 1/divisor

		if cont % 2 == 0:
			valor_teste = valor_pi - comparar
		else:
			valor_teste = valor_pi + comparar

		dif = valor_teste - valor_pi

		if dif < 0:
			dif *= -1

		if dif <= (5 * (10 ** (-8))):
			break

		valor_pi = valor_teste
		cont += 1
		divisor += 2

	return(valor_pi)

print(Pi())