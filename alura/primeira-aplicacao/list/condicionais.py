# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def validador_impar_par():
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é impar")


validador_impar_par()

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

def validador_idade():

    idade = int(input("Digite a sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Você é uma criança de", idade, "anos.")
    elif idade >= 13 and idade <= 18:
        print("Você é um adolescente de", idade, "anos.")
    elif idade > 18:
        print("Você é um adulto de", idade, "anos.")
    else:
        print("Valor inválido")


validador_idade()


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def validador_cadastro():
    usuario_correto = "itachi"
    senha_correta = 123

    usuario = input("Digite seu nome de usuário: ").lower()
    senha = int(input("Digite sua senha: "))

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem sucedido!")
    else:
        print("Login bem sucedido!")


validador_cadastro()
        
# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo 
# com as seguintes condições:
        
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem
        
def validador_coordenadas():
    eixo_x = float(input("Informe a coordenada do eixo X: "))
    eixo_y = float(input("Informe a coordenada do eixo y: "))

    if eixo_x > 0 and eixo_y > 0:
        print("O ponto está no primeiro quadrante")
    elif eixo_x < 0 and eixo_y > 0:
        print("O ponto está no segundo quadrante")
    elif eixo_x < 0 and eixo_y < 0:
        print("O ponto está no terceiro quadrante")
    elif eixo_x > 0 and eixo_y < 0:
        print("O ponto está no quarto quadrante")
    else:
        print("O ponto está sobre um eixo ou origem.")


validador_coordenadas()


def validador_coordenadas_match():
    eixo_x = float(input("Informe a coordenada do eixo X: "))
    eixo_y = float(input("Informe a coordenada do eixo y: "))

    match eixo_x and eixo_y:
        case 1 if eixo_x > 0 and eixo_y > 0:
            print("O ponto está no primeiro quadrante")
        case 2 if eixo_x < 0 and eixo_y > 0:
            print("O ponto está no segundo quadrante")
        case 3 if eixo_x < 0 and eixo_y < 0:
            print("O ponto está no terceiro quadrante")
        case 4 if eixo_x > 0 and eixo_y < 0:
            print("O ponto está no quarto quadrante")
        case _:
            print("O ponto está sobre um eixo ou origem.")

validador_coordenadas_match()