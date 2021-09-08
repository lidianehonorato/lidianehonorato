#calcular a media
nota1=float(input('digite uma media  '))
nota2=float(input('digite outra media '))
m1=(nota1 + nota2)/2
print('media é {:.2} '.format(m1))

#calcular a area
L=float(input('a largura é: '))
H=float(input('altura é: '))
a=L*H
t=a/2
print('a area é de {:.2f}m e precisara de {:.2f} litros '.format(a,t))


#calcular porcentagem
preco=float(input('digite o valor: R$  '))
print('valor original: R&  ',preco)
print('desconto ganho: R&  ',preco * 0.05)
print('valor com desconto R$: ',preco * 0.95)


