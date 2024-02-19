'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele'''
variavel = input('Insira algo para ser lido\n')
print(f'O tipo primitivo da variavel é {type(variavel)}')
print (f'A variável é um alfanumérico? {variavel.isalnum()}')
print (f'A variável é um número? {variavel.isnumeric()}')
print (f'A variável é um espaço/tem espaços? {variavel.isspace()}')
print (f'A variável tem somente letras maiúsculas? {variavel.isupper()}')
print (f'A variável tem somente letras minúsculas? {variavel.islower()}')
print (f'A variável tem letras? {variavel.isalpha()}')
print (f'A variável está capitalizada(começa com letra maiúscula)? {variavel.istitle()}')