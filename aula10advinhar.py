from random import randint
from time import sleep
pc = randint(0,5)
print('--*--' * 15)
print('vou pensar ...')
print('--*--' * 15)
n = int(input(' em que numero pensei ?  '))
print('processando...')
sleep(2)
if n == pc:
     print('parabens')
else: print('ganhei de voce, pensei em {} e voce em {}'.format(pc,n))