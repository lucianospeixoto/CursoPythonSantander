# Percorrendo Lista de Dicionários

produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900}
]

"""
Escreva um laço for que percorra essa lista e 
imprima a seguinte frase para cada item:

"O produto [nome] custa R$ [preco]"
"""
for x in produtos:
    print(f"O PRODUTO {x['nome']} CUSTA R${x['preco']}")
