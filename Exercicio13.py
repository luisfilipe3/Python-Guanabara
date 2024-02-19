'''Desafio13: Faça um algoritmo que leia o salário de um funcionário e mostre o
seu novo salário com 15% de aumento.'''
salario = float(input('Insira o seu salário: '))
salario_com_aumento = salario *1.15
print(f'O seu salário atual é R${salario:.2f} e após o aumento seu novo salário vai ser'
      f' de R${salario_com_aumento:.2f}')