"""
Para criar uma exceção personalizada, você deve criar
uma classe que herde da clase base Exception ou de 
uma de suas subclasses.
"""

def funcao():
    # Código que pode gerar exceçao personalizada
    if condicao:
        raise Exception('Descrição do erro')

try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")