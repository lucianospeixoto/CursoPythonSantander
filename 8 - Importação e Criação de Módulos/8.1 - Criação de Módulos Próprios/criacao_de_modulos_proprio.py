# Criar e utilizar módulos personalizados

"""
Para criar um módulo personalizado, simplesmente
criamos um novo arquivo Python com o nome desejado e 
definimos as funções, classes e variaveis que queremos
incluir no módulo. Por exemplo, criamos um arquivo 
(no mesmo diretorio onde estamos executando o Python)
chamado meu_modulo.py.

Podemos importar e utilizar as funções definidas em
meu_modulo.py em outro arquivo Python.
"""

import meu_modulo

meu_modulo.saudar("Luciano") # Imprime "Olá, Luciano!"
resultado = meu_modulo.calcular_soma(5,3)
print(resultado) # Imprime 8



# Organização de código em módulos

"""
A medida que nossos programas crescem em tamanho e
complexidade, é uma boa prática organizar nosso código 
em módulos separados segundo sua funcionalidade, isso
nos permite manter um código mais legivel, agrupado em
módulos e fácil de manter.

Por exemplo, podemos ter um modulo operacoes.py que 
contenha funções relacionadas com operações matematicas
e outro modulo utilidades.py que contenha funções de 
uso geral.

Depois podemos utilizar essas funções em nosso programa
principal.
"""

import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades. imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")