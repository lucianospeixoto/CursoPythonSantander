# Definição e chamada de funções

"""
Para definir uma função em Python, utiliazamos a 
palavra-chave def seguida do nome da função em 
parenteses. Opcionalmente, podemos especificar
parametros dentro dos parenteses. O bloco de
código da função é identado após os dois pontos.
"""

def saudacao():
    print("Olá, Mundo!")

saudacao()

# Parametros e Argumentos

"""
As funções podem aceitar parametros , que são 
valores que são passados para a função quando
ela é chamada. Os parâmetros são especificados
dentro dos parenteses na definição da função.
"""

def saudacao(nome):
    print("Olá, " + nome + "!")

saudacao("Luciano")
saudacao("Gabriel")

# Valores de retorno

"""
As funções podem retornar valores usando
a palavra chave return. O valor de retorno
pode ser usado pelo código que chama a função
"""

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)

# Funções anônimas (lambda)

"""
Python permite criar funções anônimas ou funções lambda
que são funções sem nome definidas em uma unica linha
São comumente usadas para funções pequenas e concisas.
"""

quadrado = lambda x: x ** 2
print(quadrado(5))

# Escopo das váriaveis (local vs. global)

"""
As variaveis definidas dentro de uma função tem
escopo local, o que significa que só são acessiveis
dentro da função. Por outro lado, as variaveis definidas
fora de qualquer função têm um escopo global e podem ser
acessadas de qualquer parte do programa.
"""

def funcao():
    variavel_local = 10
    print(variavel_local) # Acessivel dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global) #Acessivel de qlqr lugar

funcao() # Imprime 10
funcao2() # Imprime 20
print(variavel_global) # Imprime 20



# Exemplos

def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Media: ", calcular_media(10, 20, 30))

def somar_3(x):
    return x + 3

somar = lambda x: x + 3

print("Somar 3 a um numero", somar(5))


# Documentação de funções (doscstrings)

"""
É uma boa pratica documentar nossas funções
utilizando docstrings. Os docstrings são cadeias
de texto que descrevem o propósito, os parametros
e o valor de retorno de uma função. São colocados
imediatamente após a definição da função e são
encerrados entre aspas duplas triplas
"""

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.

    Args:
        base(float): A base do retângulo
        altura(float): A altura do retângulo

    Returns:
        float: A área do retângulo
    """

    return base * altura

# Funções com número váriavel de argumentos

"""
Python permite definir funções que aceitem um
número variavel de argumentos. Isso é feito utilizando
o operador * antes do nome do parâmetro
"""

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1,2,3))
print(soma_variavel(4,5,6,7))

def conta_quantidade(*numeros):
    total = 0
    for numero in numeros:
        total += 1
    return total

print(conta_quantidade(1,2,3))