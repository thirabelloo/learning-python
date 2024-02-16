# Imagine que você está desenvolvendo o sistema de backend para o "Buscante", um e-commerce especializado na venda de livros. Neste sistema, você utiliza dicionários para armazenar informações 
# sobre os livros disponíveis, com chaves representando características como título, autor e ISBN, e os valores associados a cada uma dessas chaves.

# Analise o seguinte dicionário que representa um livro no seu sistema:

livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}

# Como você faria o acesso ao preço do livro e atualizaria o valor para 69.90 utilizando o que aprendeu sobre dicionários?

livro['preco'] = 69.90         # Esta é a maneira correta de atualizar o valor associado à chave 'preco' em um dicionário em Python.
livro.update({'preco':69.90})   # O método update() é outra forma válida de atualizar o valor de uma chave em um dicionário em Python.

