nome = input ('Digite o seu nome por favor :D \n')
genero = input('Digite a letra que você mais se identifica em relação ao gênero:\n\nM para Masculino\nF para Feminino\nL para LGBTQIAP+\nNB para pessoa Não-Binária\n')
if genero == 'M' or genero == 'm':
    print(f'Seja Bem Vindo {nome}')
elif genero == 'F' or genero == 'f':
    print(f'Seja Bem Vinda {nome}')
elif genero == 'L' or genero == 'l':
    print(f'Seja Bem Vinde {nome}')
elif genero == 'NB' or genero == 'nb':
    print(f'Seja Bem Vindu {nome}')
else:
    print('Insira uma das opções sugeridas por favor.')
