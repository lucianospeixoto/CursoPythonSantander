# Entrada e sáida de dados com leitura e escrita




def maior_de_idade(idade):
    if idade >= 18:
        return "Voce e maior de idade"
    else:
        return "Voce e menor de idade"

def mostrar_dados(nome, idade):
    status = maior_de_idade(idade)
    return f"Seu nome: {nome}, sua idade: {idade} e {status}"

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

texto_final = mostrar_dados(nome, idade)

arquivo = open("dados3.txt", "w")
arquivo.write(texto_final)
arquivo.close()
arquivo = open("dados3.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()