import math
angulo = float(input('digite um angulo:  '))

seno = math.sin(math.radians(angulo))
print('o valor {} de seno  {:.2f}'.format(angulo,seno))
tangente = math.tan(math.radians(angulo))
print('o valor {} da tangente é {:.2f} '.format(angulo, tangente))
cosseno = math.cos(math.radians(angulo))
print('o valor {} do cosseno é {:.2f} '.format(angulo,cosseno))