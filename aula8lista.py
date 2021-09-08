import random

import lista as lista

n1 = str(input('aluno: '))
n2 = str(input('aluno: '))
n3 = str(input('alumo: '))
n4 = str(input('aluno: '))

lista=[n1,n2,n3,n4]

random.shuffle(lista)
print('ordem escolhido é ')
print(lista)
