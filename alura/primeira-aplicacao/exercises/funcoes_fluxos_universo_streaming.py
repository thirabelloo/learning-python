# Imagine que você está desenvolvendo um projeto para um serviço de streaming de música. Sua tarefa é melhorar o algoritmo de recomendação de músicas, 
# garantindo que os usuários recebam sugestões mais precisas com base em seus gêneros favoritos. Para isso, você precisa criar uma função em Python que classifique as 
# sugestões de músicas utilizando estruturas condicionais if, else e elif.

# No processo de desenvolvimento, você escreveu a seguinte função para classificar uma música como 'recomendada', 'neutra' ou 'não recomendada' com base na 
# preferência do gênero musical do usuário:

# def classificar_musica(genero_favorito, genero_musica):
#     if genero_favorito == genero_musica:
#         return 'recomendada'
#     elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
#         return 'neutra'
#     else:
#         return 'não recomendada'

# resultado = classificar_musica('Rock', 'Pop')
# print(resultado)


# Após analisar a função, determine qual será a saída se o gênero favorito do usuário for 'Rock' e o gênero da música for 'Pop'.


def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)