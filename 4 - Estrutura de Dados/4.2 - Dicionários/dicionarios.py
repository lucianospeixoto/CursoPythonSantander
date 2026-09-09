# Criação e acesso

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

"""
Para acessar os valores de um dicionario, utilize a
chabe correspondente entre colchetes:
"""

print(pessoa["nome"]) # Imprime "João"
print(pessoa["idade"]) # Imprime 25
print(pessoa["cidade"]) # Imprime "Madri"

"""
Você também pode utilizar o método get() para
obter o valor de uma chave. Se a chave não existir,
retorna um valor padrão (por padrão, None).
"""



# Métodos de Dicionarios

"""
Os dicionarios em Python têm vários métodos
incorporados para manipular e acessor os elementos.
Alguns métodos comuns são:

keys(): retorna uma visualização de todas as chaves
do dicionario.

values(): retorna uma visualização de todos os valores
do dicionario.

items(): retorna uma visualização de todos os pares 
chave-valor do dicionario.

update(outro_dicionario): atualiza o dicionario com
os pares chave-valor de outro dicionário.

Exemplo:
"""

pessoa = {"nome": "João",
          "idade": 25,
          "cidade": "Madri"}

print(pessoa.keys()) # Imprime dict_keys(["nome", "idade", "cidade"])

print(pessoa.values()) # Imprime dict_values(["João", 25, "Madri"])

print(pessoa.items()) # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])

pessoa.update({"profissao": "Engenheiro"})
print(pessoa) # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}



# Para criar um dicionario com mais pessoas deve criar uma lista

# Lista contendo 3 dicionarios (3 pessoas)

pessoas = [
    {"nome": "Luciano", "idade": 19, "cidade": "Franca"},
    {"nome": "Leonardo", "idade": 20, "cidade": "Campinas"},
    {"nome": "Martim", "idade": 21, "cidade": "Lisboa"},
    {"nome": "Pedro", "idade": 18, "cidade": "Curitiba"}
]

# Acessando a primeira pessoa (indice 0) e o nome dela:
print(pessoas[0]["nome"])

# Acessando a cidade da segunda pessoa:
print(pessoas[1]["cidade"])

# Mostrando todos os dados do dicionario
x = 0

while x < len(pessoas):
    print(pessoas[x])
    x += 1