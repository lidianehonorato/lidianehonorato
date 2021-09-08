#calcular reajuste salarial

salario= float(input('qual o seu salario? '))
novo= salario +(salario * 0.15)
print('o salario era de {:.2f} e agora sera {:.2f}'.format(salario,novo))

#converter temperatura
c= float(input('qual a temperatura atual?  '))
f= ((9 * c) / 5) + 32
print('a temepratura é {}ºC em fareight é {}ºf'.format(c,f))