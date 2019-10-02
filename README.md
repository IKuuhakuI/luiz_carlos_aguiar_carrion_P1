<H1> CORREÇÃO DA PROVA </H1>

<H2> Questão 1 </H2>
<p> Nessa questão, o código ficou igual ao feito em sala. <br>
	A lógica foi simples, simplesmente eu verificava o delta 
	e se ele fosse maior ou igual a zero, eu utilizei a fórmula de 
	bháskara normalmente. Caso fosse menor que 0, eu separei em duas
	partes. A parte inteira foi calculada como sendo (-b) / (2*a). 
	Já a parte imaginária foi tirada a raiz do módulo de delta 
	e esse valor foi divido por 2 * a. Por fim, só alternei o sinal
	do valor encontrado para ter as duas raízes. </p>

<H2> Questão 3 </H2>
<p> Nessa questão, o código teve algumas diferenças se comparado ao 
	feito em sala. A única diferença foi o fato de eu ter esquecido
	de multiplicar por 4 o valor encontrado na série, assim retornando
	o valor de PI/4, e não o valor de PI.<br>
	Mesmo com essa correção, a lógica não mudou muito. Para calcular
	o valor da série, iniciamos no valor 1. A variável cont serve para
	saber qual o sinal atual (+ ou -). divisor é o próximo número da série,
	visto que todos seguem o padrão, 1/(n+2*cont), sendo o n = 1. A variável
	comparar é o próximo valor a ser somado/diminuído na série. O sinal é calculado
	pelo módulo. Se cont for par, o sinal é -. Caso seja ímpar, o sinal é +. no caso 
	da diferença ser negativa, ele multiplica ela por -1. logo depois, ele compara a 
	diferença com 5 * 10**-8. Caso seja menor, ele para o loop. Caso o loop continue,
	o valor_pi é atualizado para o valor que foi encontrado, o contador é incrementado
	em 1 e o divisor é incrementado em 2. Ao final, ele retorna 4 * o valor de pi. </p>

<H2> Questão 4 </H2>
<p> Nessa questão, o código ficou igual ao feito em sala. <br>
	Basicamente, temos que saber os algarismos da dezenas e das
	unidades de cada número. Logo eu verifiquei se o número era
	maior que 10. Caso sim, ele iria fazer várias subtrações (-10) até
	que isso fosse falso. A quantidade de vezes q ele subtraiu é o 
	algarismo das dezenas. O que sobrar são as unidades. Por fim, só
	somei tudo e retornei esse valor. Na main, como ele queria achar o
	algarismo 12, eu criei uma lista com os valores fornecidos pelo problema.
	Assim, enquanto o algarismo não fosse 12, ele iria ficar rodando a função
	várias vezes. </p>