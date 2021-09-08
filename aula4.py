#mostrar numero inteiro, antecessor e sucessor

a=int(input('digite um numero  ' ))
at=a-1
su=a+1
print('o valor é {} o antecessor é {} e o sucessor é {}'.format(a,at,su))

#converter moeda

real= float(input('quanto vc tem na carteira R$ '))
dolar = real / 3.50
print('com R$ {:.2f} voce pode comprar US${:0.2f}'.format(real,dolar))

