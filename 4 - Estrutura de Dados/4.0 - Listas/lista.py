# Criação e acesso

"""
Para criar uma lista, simplesmente
encerre os elementos entre colchetes:
"""

frutas = ["maça", "banana", "laranja"]

"""
Para acessar os elementos de uma lista
utilize o indice do elemento entre colchetes.
Os indices começam a partir de 0.
"""

print(frutas[0]) # maça
print(frutas[1]) # banana
print(frutas[2]) # laranja

"""
Você também pode acessar os elementos a partir
do final da lista utilizando inidices negativos.
O indice -1 representa o ultimo elemento, -2 representa 
o penultimo e assim por diante.
"""

print(frutas[-1]) # laranja
print(frutas[-2]) # banana
print(frutas[-3]) # maça

# Metodos de Listas

"""
As listas em Python têm vários métodos incorporados
que nos permitem manipular e modificar os elementos
da lista. Alguns métodos comuns são:

append(elemento): adiciona um elemento ao final da lista.

insert(indice, elemento): insere um elemento
em um aposição especifica na lista.

remove(elemento): remove a primeira ocorrencia
de um elemento na lista.

pop(indice): remove e retorna o elemento em uma
posição especifica da lista.

sort(): ordena os elementos da lista de forma
ascendente.

reverse(): inverte a ordem dos elementos na lista.

exemplo:
"""

frutas = ["maça", "banana", "laranja"]

frutas.append("pera")
print(frutas) # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas) # Imprime ["maçã", "uva", "banana","laranja", "pera"]

frutas.remove("banana")
print(frutas) # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas) # Imprime ["maçã", "uva", "pera"]
print(fruta_removida) # Imprime "laranja"

frutas.sort()
print(frutas) # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas) # Imprime ["uva", "pera", "maçã"]


#Teste para colocar ABC em ordem e reverse
nomes = ["c", "b", "a", "f", "d", "e"]
print(nomes)

nomes.append("g")
print(nomes)

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)


# Lista de compreensão

"""
As listas de compreensão são uma
forma concisa de criar novas listas baseadas
em uma sequência existente. Permitem filtrar
e transformar os elementos de uma lista em uma
única linha de código.

nova_lista = [expressão for elemento in
    sequencia if condição]

exemplo:
"""

numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros if x
             % 2 == 0]
print(quadrados)