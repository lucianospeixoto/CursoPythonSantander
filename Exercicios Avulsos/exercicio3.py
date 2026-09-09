# Atualizando Dicionário

"""
Crie um dicionário chamado aluno com as chaves
 "nome", "curso" e "nota".

Imprima apenas o valor da chave "nome".

Em seguida, use o método .update() para adicionar
a chave "status" com o valor "Aprovado".
"""

aluno = {"nome": "Luciano",
         "curso": "ADS",
         "nota": 6}

print(aluno["nome"])

aluno.update({"status": "Aprovado"})

print(aluno)