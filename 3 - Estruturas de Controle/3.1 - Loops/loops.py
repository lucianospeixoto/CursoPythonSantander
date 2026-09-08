# For

"""
O loop for é utilizado para iterar sobre uma
sequência (como uma lista, uma tupla ou uma string) 
ou qualquer objeto iterável. 
A sintaxe básica é a seguinte

for variavel in sequencia:
    Bloco de código a repetir instruções

exemplo:
"""

frutas = ["maça", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

print ("Numeros de 1 a 5 multiplicados por 2:")
for numero in range(1, 6):
    print (numero * 2)


# While

"""
O loop while é utilizado para repetir um bloco de código 
enquanto uma condição for verdadeira. 
A sintaxe básica é a seguinte:

while condicao:
    Bloco de código a repetir instruções

exemplo:
"""

contador = 0

while contador < 5:
    print(contador)
    contador += 1


print ("\nNúmros de 1 a 5 multiplicados por 2:")
contador = 1
while contador <= 5:
    print (contador * 2)
    contador += 1


# Controle de loops

# Break

"""
A instrução break é utilizada para sair prematuramente 
de um loop, independentemente da condição. 
Quando um break é encontrado,
o loop é interrompido e o fluxo de execução continua 
com a próxima instrução fora do loop.
"""

contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break  # Sai do loop quando o contador atingir 5


# Númros de 1 a 10 multiplicados por 2 usando break
print ("\nNúmeros de 1 a 10 multiplicados por 2:")
contador = 1
while True:
    print(contador * 2)
    contador += 1

    if contador > 10:
        break  # Sai do loop quando o contador atingir 10



# Continue

"""
A instrução continue é utilizada para pular o restante do
bloco de código
dentro de um loop e passar para a próxima iteração.

exemplo:
"""

for i in range(10):
    if i % 2 == 0:
        continue  # Pula a iteração atual se i for par
    print(i)  # Isso só será executado para números ímpares




# Pass

"""
A instrução pass é uma operação nula que não faz nada. 
É utilizada como um marcador de posição quando uma 
instrução é 
sintaticamente necessária, mas nenhuma ação é desejada.

exemplo:
"""

for i in range(5):
    pass  # Não faz nada, apenas passa para a próxima iteração
