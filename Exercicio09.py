'''Desafio09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada'''
from colorama import init, Fore, Back

init()

numero = int(input('Insira o número que deseja ver a tabuada de 10: '))
print(f'{numero} * 1 = {numero*1}')
print(f'{numero} * 2 = {numero*2}')
print(f'{numero} * 3 = {numero*3}')
print(f'{numero} * 4 = {numero*4}')
print(f'{numero} * 5 = {numero*5}')
print(f'{numero} * 6 = {numero*6}')
print(f'{numero} * 7 = {numero*7}')
print(f'{numero} * 8 = {numero*8}')
print(f'{numero} * 9 = {numero*9}')
print(f'{numero} * 10 = {numero*10}')
print(Fore.YELLOW + 'Seus cálculos da sua tabuada de 10 tiveram resultados iguais?')
resposta = input('Insira a letra "S" para confirmar e a letra "N" para negar\n')
if resposta == 'S':
    print(Fore.GREEN + 'Parabéns seus cálculos estão corretos')
elif resposta == 'N':
    print(Fore.RED + 'Desculpe seus cálculos não estão corretos, tente novamente')
else:
    print('Insira a letra "S" ou "N". Por favor')