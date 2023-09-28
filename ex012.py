
#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Preço do produto: '))
disconto_produto = float(input('Disconto em porcentagem: '))
valor_disconto = preco_produto-((preco_produto*disconto_produto)/100)

print('O seu produto custa R${} , com o disconto de {}% , o produto fica R${:.2f} .'.format(preco_produto , disconto_produto , valor_disconto))