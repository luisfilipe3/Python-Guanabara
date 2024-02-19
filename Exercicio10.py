'''Desafio10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar. Considere U$1,00 = R$3,27'''
#Converte real para dólar
real = float(input('Insira a quantidade em reais a ser convertida para Dólares: '))
dolar = real /3.27
print(f'O seu dinheiro em reais é R${real:.2f} e o valor convertido em dólar é U${dolar:.2f}')