# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

def criando_dicionario():
    pessoa = {'Nome': 'Thiago', 'Idade': 29, 'Cidade': 'São Paulo'}
    print(pessoa)


# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

def brincando_dicionario():

    pessoa = {'Nome': 'Thiago', 'Idade': 29, 'Cidade': 'São Paulo'}
    print(pessoa)

    pessoa['Idade'] = 30  # Modifique o valor de um dos itens, atualize a idade da pessoa
    print(pessoa)

    pessoa['Profissão'] = 'Engenheiro'  # Adicione um campo de profissão para essa pessoa.
    print(pessoa)

    del pessoa['Cidade']    # Remova um item do dicionário.
    print(pessoa)


# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

def numero_quadrado():
    numeros_quadrados = {x: x**2 for x in range(1,6)}
    print(numeros_quadrados)



# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

def validador_dicionario():

    pessoa = {'Nome': 'Thiago', 'Idade': 29, 'Cidade': 'São Paulo'}

    if 'Nome' in pessoa:
        print("A chave 'Nome' existe no dicionário.")
    else:
        print("A chave 'Nome' não existe no dicionário.")


# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

def contar_frequencia(e):
    frase = 'Eu estou estudando para Python e estou animado'
    frequencia = {}
    palavras = frase.split()

    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    print(frequencia)



