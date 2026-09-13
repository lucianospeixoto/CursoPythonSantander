# Importar módulos

"""
Para utilizar um módulo em nosso programa, devemos 
importa-lo utilizando a declaração import. Podemos
importar um módulo completo ou funções especificas
de um módulo.
"""

import math

resultado = math.sqrt(25)
print(resultado) # Imprime 5.0

"""
Neste exemplo, importa-se o módulo math utilizando
a declaração import. Em seguida, utiliza-se a função
sqrt() do módulo math para calcular a raiz quadrada
de 25

Também podemos importar funções especificas de um módulo
utilizando a sintaxe from módulo import função
"""

from math import sqrt

resultado = sqrt(25)
print(resultado) # Imprime 5.0

"""
Neste caso, importa-se apenas a função sqrt() do módulo
math, o que nos permite utiliza-la diretamente sem ter 
que precede-la com o nome do  módulo.
"""



# Funções e classes de módulo padrão

"""
A bibilioteca padrão de Python oferece uma ampla gama
de módulos com funções e classes uteis. 
Alguns exemplos comuns incluem:
"""

# Math
"""
Fornece funções matemáticass, como sqrt()(raiz quadrada)
, sin()(seno), cos()(cosseno), entre outras.
"""
# Random
"""
Oferece funções para gerar números aleatórios, como 
random()(numero aleatorio entre 0 e 1),
randint()(numero inteiro aleatorio em um intervalo),
entre outras.
"""
# Datetime
"""
Permite trabalhar com datass e horas, como datetime.now()
(data e hora atual), datetime.date()(data), datetime.time()
(hora), entre outras.
"""

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) # Imprime um numero inteiro aleatorio entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual) # Imprime a data e hora atual
