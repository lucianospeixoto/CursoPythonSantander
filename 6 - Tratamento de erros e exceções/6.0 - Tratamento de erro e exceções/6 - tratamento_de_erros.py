# Erros comuns em Python

"""
Antes de mergulharmos no tratamento de exceções,
vejamos alguns erros comuns que você pode encontrar
em Python
"""

# Erro de Sintaxe (SyntaxError)

"""
Ocorre quando o código não segue
as regras de sintaxe do Python, como esquecer
dois pontos após uma declaração de função
ou um loop
"""

def minha_funcao() # Faltam dois pontos
    print("Olá")



# Erro de nome(NameError)

"""
Ocorre quando se faz referencia a uma variavel
ou função que não foi definida
"""

print(variavel_nao_definida)



# Erro de tipo(TypeError)

"""
Ocorre quando se realiza uma operação com tipos de
dados incompativeis, como tentar somar um numero e uma
string.
"""

resultado = 5 + "10"



# Erro de indice{IndexError}

"""
Ocorre quando se tenta acessar um indice fora
do intervalo valido de uma lista ou sequencia
"""

lista = [1,2,3]
print(lista[3]) # O indice 3 está fora do intervalo



"""
Estes são apenas alguns exemplos de erros comuns. 
Quabdo ocorre um erro, Python gera uma exceção
e exibe uma mensagem de erro que inclui o tipo de
exceção e uma descrição do problema.
"""