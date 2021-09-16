dist = float(input('qual a distancia da viagem?   '))
print(' Sua viagem de {} km vai começar!! '.format(dist))
if dist <=200:
    preço = dist * 0.50
    print(' Voce pagara este valor {:.2f} por ate 200 km! '.format(preço))
else:
    preço = dist * 0.45
    print(' Voce pagara este valor {:.2f} por ultrapassar 200 km!'.format(preço))