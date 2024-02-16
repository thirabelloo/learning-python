# Imagine que você está desenvolvendo em Python para a Meteora, uma loja de roupas e-commerce. Você está no processo de adicionar descrições de produtos ao site e precisa usar a função print em python
# para exibir as descrições na página. As descrições dos produtos incluem várias linhas e parágrafos.

# Quais das seguintes opções você escolheria para imprimir corretamente uma descrição de produto de várias linhas usando a função print em Python?

print('''Camiseta Unissex
Tamanho: P, M, G, GG
Material: 100% algodão
Cores disponíveis: Preto, Branco, Vermelho''')  #As aspas triplas (''' ou """) são usadas para criar strings que abrangem várias linhas. Elas são úteis quando você precisa incluir quebras de linha e manter o formato do texto.



print('\n')
print("Camiseta Unissex","Tamanho: P, M, G, GG","Material: 100% algodão","Cores disponíveis: Preto, Branco, Vermelho", sep ='\n') # Com o uso de várias strings com o separador ‘sep’ indicando a quebra de linha entre cada uma delas, cada string será impressa com espaçamentos e quebras de linha.