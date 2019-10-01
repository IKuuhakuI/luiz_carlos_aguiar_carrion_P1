def nob(valor_1, valor_2):
	dezenas_v1 = 0
	unidades_v1 = 0
	dezenas_v2 = 0
	unidades_v2 = 0

	while valor_1 >= 10:
		valor_1 -= 10
		dezenas_v1 += 1
	while valor_2 >= 10:
		valor_2 -= 10
		dezenas_v2 += 1

	unidades_v1, unidades_v2 = valor_1, valor_2

	soma = unidades_v1 + unidades_v2 + dezenas_v1 + dezenas_v2

	return soma

def main():
	num = 72
	valores = [99, 45, 39, 36]

	cont = 0

	while num != 12:
		temp = num
		num = nob(temp,valores[cont])

		cont += 1

	print("Resultado:", num)
	

main()