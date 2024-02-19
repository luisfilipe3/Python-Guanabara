'''Desafio11 Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados'''
#Leia a altura e largura, calcule a área e a quantidade de tinta
#cada litro pinta 2 metros quadrados
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area_quadrada = largura * altura
tinta_litro = area_quadrada/2
print(f'A largura da parede é {largura} e a altura é {altura}. A área quadrada é '
      f'{area_quadrada} Metros quadrados.\nO necessário em litros de tinta para pintar é {tinta_litro} L de tinta')