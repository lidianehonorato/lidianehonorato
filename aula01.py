#mostrar os resultados aritmeticos

n1=int(input('digite um numero:  '))
n2=int(input('digite outro numero:  '))
s=n1+n2
m=n1 *n2
d= n1/n2
di= n1//n2
e=n1**n2
print('o valor a soma é: {} o produto vale: {} e a divisao vale: {:.2f}'.format(s,m,d))
print('a divisao inteira vela:{} e a potencia vale:{}'.format(di,e))