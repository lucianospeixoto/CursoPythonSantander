# Criação e acesso

"""
Para criar uma tupla, encerre os elementos entre 
parênteses:
"""

ponto = (3,4)

"""
Para acessar os elementos de uma tupla
utilize o indice do elemento entre colchetes,
similar às listas:
"""

print(ponto[0]) # Imprime 3
print(ponto[1]) # Imprime 4

# Metodos de tuplas


# Index
"""
Embora as tuplas sejam imutaveis, Python fornece
vários métodos uteis para trabalhar com elas:

count(elemento): Devolve o numero de vezes que 
um elemento aparece na Tupla.

index(elemento): Devolve o indice da primeira
aparição de um elemetno na tupla. Opcionalmente, pode-se
especificar no inicio e fim da busca.

len(tupla): Embora não seja um método de tupla 
propriamente dito, esta função incorporada devolve
o comprimento da tupla.
"""

minha_tupla = (1, 2, 3, 2, 4, 2)


"""
# minha_tupla.index( O_QUE_BUSCAR )

O que você pediu: "Em qual posição está o número 2?"

Como o Python age: Ele começa a procurar do início. 
Encontra o primeiro número 2 logo na posição 1.

Resultado: 1.

Exemplo:
"""
print (minha_tupla.index(2)) # Sáida 1



"""
# minha_tupla.index( O_QUE_BUSCAR , ONDE_COMEÇAR )

O que você pediu: "Procure o valor 2, COMEÇANDO a 
busca a partir do índice 2."

Como o Python age: Ele ignora o início (índices 0 e 1) 
e passa a olhar do índice 2 em diante. O próximo número 2 
que ele encontra está no índice 3.

Resultado: 3.

Exemplo:
"""
print (minha_tupla.index (2, 2)) # Sáida 3



"""
# minha_tupla.index( O_QUE_BUSCAR , ONDE_COMEÇAR , ONDE_PARAR )

O que você pediu: "Procure o valor 2, 
começando no índice 2 e PARANDO ANTES do índice 4."

Como o Python age: Ele só vai olhar a "fatia" entre 
os índices 2 e 3 (ele não inclui o índice limite 4). 
Dentro dessa fatia, o número 2 está no índice 3.

Resultado: 3.

Exemplo:
"""

print (minha_tupla.index(2, 2, 4)) #Sáida 3




# Count

"""
O .count(elemento) funciona como um contador: ele
percorre a tupla inteira e devolve quantas vezes o valor
fornecido aparece.
"""

minha_tupla = (1, 2, 3, 2, 4, 2)

"""
Quantas vezes o número 2 aparece na Tupla?
"""
print(minha_tupla.count(2)) # Saída: 3



"""
Quantas vezes o número 4 aparece na Tupla?
"""
print(minha_tupla.count(4)) #Saída: 4



"""
Quantas vezes o número 9 aparece na Tupla?
"""
print(minha_tupla.count(9)) # Saída: 0 
# (Se não existir ele retorna 0 sem dar erro)




# Len

"""
O len() é uma função do próprio Python que diz
quantos itens no total existem dentro da tupla.
"""

minha_tupla = (1, 2, 3, 2, 4, 2)

"""
Quantos elementos existem no total dentro dessa
tupla?
"""
print(len(minha_tupla)) #Saída: 6