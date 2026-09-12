# Leitura de arquivos

"""
Para ler o conteudo de um arquivo, primeiro devemos
abri-lo utilizando a função open() em modo de leitura("r")
Depois, podemos ler o conteudo do arquivo utilizando os
metodos como read() ou readlines().
"""

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()



# Escrita de arquivos

"""
Para escrever dados em um arquivo, abrimos em modo de
escrita ("w") utilizando a função open(). Se o arquivo
não existir, será criado automaticamente. Se o arquivo
já existir, seu conteudo será sobrescrito.
"""

arquivo = open("dados2.txt", "w")
arquivo.write("Ola, mundo lindo!")
arquivo = open("dados2.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()



"""
Importante

É importantes fechar os arquivos depois de utiliza-los
para liberar recursos do sistema.

Você também pode utilizar a declaração with para manejar
a abertura e fechamento de arquivos de maneira
automatica.
"""

with open("dados2.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"""
Neste caso, o arquivo é aberto utilizando a declaração
with e é fechado automaticamente uma vez que sai do
bloco with, mesmo se ocorrer uma exceção.
"""