# Estruturas Condicionais

"""
As estruturas condicionais 
nos permitem executar diferentes blocos de 
código segundo se cumpra ou não uma determinada 
condição. Em Python, as estruturas condicionais
mais utilizadas são if, if-else e if-elif-else.

IF

if condicao:
    Bloco de código a executar se a condição for
    verdadeira
    instruções

exemplo:
"""

idade = 18

if idade >= 18:
    print ("Você é maior de idade.")




"""
IF-ELSE

A estrutura if-else nos permite especificar um 
bloco de código alternativo que será executado se a 
condição do if for falsa.
A sintaxe básica é a seguinte:
"""

idade2 = 15

if idade2 >= 18:
    print ("Você é maior de idade.")
else:
    print ("Você é menor de idade.")




"""
IF-ELIF-ELSE

A estrutura if-elif-else nos permite especificar 
múltiplas condições e blocos de código alternativos.
A sintaxe básica é a seguinte:

if condicao1:
    Bloco de código a execurar se a condicao1 for 
    verdadeira
    instruções
elif condicao2:
    Bloco de código a executar se a condicao2 for
      verdadeira
    instruções
else:
    Bloco de código a executar se todas as condições 
    forem falsas
    instruções

exemplo:
"""

nota = 85

if nota >= 90:
    print ("Excelente")
elif nota >= 80:
    print ("Muito bom")
elif nota >= 70:
    print ("Bom")
else:
    print ("Precisa melhorar")




idade3 = 20

if idade3 < 18:
    print ("Você é menor de idade.")

elif idade3 >=18 and idade3 < 60:
    print ("Você é adulto.")

elif idade3 > 15:
    print ("Você é maior de 15 anos.")

elif idade3 == 60:
    print ("Feliz aniversário de 60 anos!")

else:
    print ("Você é idoso.")