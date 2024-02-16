# Você está criando seu portfólio para mostrar seus projetos de Python. Para isso, você quer incluir uma seção que destaque suas habilidades com listas, loops for e 
# tratamento de exceções, mas quer garantir que mesmo que algum dado esteja ausente, seu portfólio não quebre.

# Analise o código abaixo e julgue as opções, selecionando a que melhor implementa o uso de listas, blocos for e try except.

# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]


# Qual trecho de código você deveria incluir para iterar seguramente pela lista de projetos?


projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto:
        print(f"Projeto: {projeto}")
    else:
        print("Projeto não disponível.")

# Esta opção utiliza um loop for para iterar através dos elementos da lista projetos e, em seguida, usa um bloco if para verificar se o valor do projeto é diferente de None antes de imprimir.
#  Isso evita problemas de TypeError e trata explicitamente a condição de projeto não disponível.