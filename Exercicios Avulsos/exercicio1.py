# Filtrando uma Lista com List Comprehension

"""
Dada a lista idades = [15, 22, 12, 19, 30, 17, 25], 
crie uma list comprehension que gere uma nova lista 
apenas com as idades maiores ou iguais a 18 anos.
"""

idades = [15, 22, 12, 19, 30, 17, 25]
maiores = [x for x in idades if
           x >= 18]
print(maiores)




