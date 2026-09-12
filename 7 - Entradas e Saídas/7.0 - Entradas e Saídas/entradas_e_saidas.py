# Entrada de dados do usuário

"""
Para obter informações do usuario durante a execução
do programa, podemos utilizar a função input().
Esta função mostra uma mensagem na tela e espera que o 
usuario insira um valor.
"""

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá," + nome + "!")
print("Você tem " + idade + " anos.")

"""
Importante

A função input() sempre retorna uma cadeia de texto
Se você deseja trabalhar com outros tipos de dados, como
numeros inteiros ou flutuantes, deve realizar uma
conversão explicita utilizando funções como int() ou 
float()
"""
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")



# Saída de dados

"""
Para mostrar informações na tela, utilizamos a função
print(). Esta função recebe um ou mais argumentos e os
mostra no console.

Podemos utilizar a f-string (formatação de cadeias)
para inserir variaveis diretamente dentro de uma cadeia
de texto
"""
nome = "Juan"
idade = 25

print(f"Olá, meu nome é {nome} e tenho {idade} anos")