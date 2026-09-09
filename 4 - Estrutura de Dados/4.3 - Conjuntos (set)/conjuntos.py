# Criação e operações básicas

frutas = {"Maçã", "Banana", "Laranja"}
numeros = set([1, 2, 3, 4, 5])

"""
Os conjuntos suportam operações matemáticas de
conjuntos, como a união (|),a interseção (&), 
a diferença (-) e a diferença simétrica (^).
"""

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)

intersecao = conjunto1 & conjunto2
print(intersecao)

diferenca = conjunto1 - conjunto2
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)


# Métodos de conjuntos

"""
Os conjuntos em Python têm vários métodos incorporados
para manipular e acessar os elementos. Alguns métodos
comuns são:

add(elemento): Adiciona um elemento ao conjunto.

remove(elemento): Remove um elemento do conjunto.
Se o elemento não existir gera um erro.

discard(elemento): Remove um elemento do conjunto se
estiver presente. Se o elemento não existir não faz nada

clear(): Remove todos os elementos do conjunto

Exemplo:
"""

frutas = {"Maça", "Banana", "Laranja"}

frutas.add("Pera")
print(frutas)

frutas.remove("Banana")
print(frutas)

frutas.discard("Uva")

frutas.clear()
print(frutas)