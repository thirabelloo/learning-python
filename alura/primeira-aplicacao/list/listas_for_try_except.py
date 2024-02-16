# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

def criacao_listas():

    lista_numeros = [1,2,3,4,5,6,7,8,9,10]
    lista_nomes = ["Thiago", "Lucas", "Paulo", "Alfredo"]
    lista_ano = [1994, 2024]


# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

def percorendo_listas():
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]

    for numeros in lista_numeros:
        print(numeros)


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

def soma_numeros_impares():
    soma_impares = 0

    for numero_impar in range(1, 11, 2):
        soma_impares += numero_impar
    print(f"O resultado da soma dos números ímpares é: {soma_impares}")


def soma_numeros_impares_outra_forma():
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]
    soma = 0

    for numeros_impar in lista_numeros:
        if numeros_impar %2 != 0:
            soma += numeros_impar
    print(f"O resultado da soma dos números ímpares é: {soma}")



# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
    
def imprime_ordem_descrescente():
    for numeros_descrecente in range(10, 0, -1):
        print(numeros_descrecente)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

def tabuada(numero_usuario):
    print(f"Tabuada do número {numero_usuario}")
    for multiplica in range(1,11):
        resultado =  multiplica * numero_usuario
        print(f"{multiplica} X {numero_usuario} = {resultado}")


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

def soma_lista():
    lista = [0,10,20,30,40,50,60,70,80,90,100]
    soma = 0

    try:
        for numero in lista:
            soma += numero
        print(f"Soma dos elementos: {soma}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

def calcula_media():

    lista = [0,10,20,30,40,50,60,70,80,90,100]
    soma = 0
    media = 0

    try:
        for valor in lista:
            soma += valor
        media = soma / len(lista)
        print(f"Soma dos elementos: {soma}")
        print(f"Média dos elementos {media}")
        
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
            
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
