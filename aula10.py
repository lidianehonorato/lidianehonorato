tempo = int(input('quantos anos tem o seu carro?  '))
if tempo <=3:
    print('carro novo')
else: print('carro velho')
print('--fim---')


# segunda forma de montar a solução codigo simplificado
tempo = int(input('quantos anos tem o seu carro?  '))
print('carro novo' if tempo <=3 else'carro velho')
print('--fim---')