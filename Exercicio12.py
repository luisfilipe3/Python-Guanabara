'''Desafio12: Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço com 5% de desconto.'''
valor_produto = float(input('Insira o valor do produto que deseja saber o valor após o desconto: '))
produto_com_desconto = valor_produto *0.95
print(f'O valor do produto sem desconto é R${valor_produto}'
      f' e o valor do produto com desconto é R${produto_com_desconto}')