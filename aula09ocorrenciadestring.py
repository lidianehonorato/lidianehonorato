frase = str(input('digite uma frase  ')).lower().strip()

print('a letra aparece {} vezes'.format(frase.count('a')))
print('a primeira  aparece na posição {} '.format(frase.find('a')+1))
print(' a ultima letra aparece na posiçao {} '.format(frase.rfind('a')+1))

