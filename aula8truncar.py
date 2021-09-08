import math

#num = float(input('digite um numero:  '))
#valor = math.trunc(num)
#print('o valor é {} e sua parte inteira é: {}  '.format(num,valor))

ca = float(input('digite um valor:  '))
co = float(input('digite outro valor: '))
soma = (ca**2 + co**2) **(1/2)
print('o valor da hipotenusa é {:.2f}'.format(soma))

# usando a importação do hipot do modulo math.
ca = float(input('digite um valor:  '))
co = float(input('digite outro valor: '))
hi= math.hypot(ca,co)
print('o valor da hipotenusa é {:.2f}'.format(hi))