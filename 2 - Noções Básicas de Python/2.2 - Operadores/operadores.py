# Aritméticos

"""
Os operadores aritméticos são utilizados para 
realizar operações matemáticas básicas. 
Os principais operadores aritméticos em Python são:

Soma (+): Adiciona dois valores.

Subtração (-): Subtrai um valor de outro.

Multiplicação (*): Multiplica dois valores.

Divisão (/): Divide um valor pelo outro e 
devolve um número de ponto flutuante (float).

Divisão inteira (//): Realiza a divisão e 
retorna apenas a parte inteira do resultado.

Módulo (%): Retorna o resto da divisão entre dois valores.

Exponenciação (**): Eleva um valor à potência de outro.

Exemplos:
"""

a = 10
b = 3

soma = a + b # Resultado: 13
subtracao = a - b # Resultado: 7
multiplicacao = a * b # Resultado: 30
divisao = a / b # Resultado: 3.3333333333333335
divisao_inteira = a // b # Resultado: 3
modulo = a % b # Resultado: 1
exponenciacao = a ** b # Resultado: 1000



# De comparação

"""
Os operadores de comparação são utilizados para 
comparar dois valores e devolvem um valor booleano 
(True ou False) segundo o resultado da comparação. 
Os operadores de comparação em Python são:

Igual a (==): 
devolve True se ambos os valores são iguais.

Diferente de (!=): 
devolve True se os valores são diferentes.

Maior que (>):
devolve True se o primeiro valor é maior que o segundo.

Menor que (<): 
devolve True se o primeiro valor é menor que o segundo.

Maior ou igual que (>=): 
devolve True se o primeiro valor é maior ou igual 
que o segundo.

Menor ou igual que (<=): 
devolve True se o primeiro valor é menor ou igual 
que o segundo.

Exemplos:
"""

a = 10
b = 3

igual = a == b # Resultado: False
diferente = a != b # Resultado: True
maior_que = a > b # Resultado: True
menor_que = a < b # Resultado: False
maior_ou_igual = a >= b # Resultado: True
menor_ou_gual = a <= b # Resultado: False



# Lógicos

"""
Os operadores lógicos são utilizados para 
combinar expressões condicionais e avaliar 
múltiplas condições. 
Os operadores lógicos em Python são:

AND(and): devolve True se ambas as condições 
forem verdadeiras.

OR(or): devolve True se pelo menos uma 
das condições for verdadeira.

NOT(not): inverte o valor lógico de uma condição, 
devolvendo True se a condição for 
falsa e False se a condição for verdadeira.

Exemplos:
"""

a = 10
b = 3

resultado_and = (a > 5) and (b < 5) # Resultado: True
resultado_or = (a > 15) or (b < 5) # Resultado: True
resultado_not = not (a > 5) # Resultado: False
