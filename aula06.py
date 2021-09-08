#criar uma tabuada

valor= int(input('entre com o numero para tabuada  '))
aux=0
print('*' * 18)
print('tabuada de {}'.format(valor))
print('*' * 18)

while (aux <=10):
    print('{0} X {1} = {2}'.format (aux,valor,(aux * valor)))
    aux = aux +1
