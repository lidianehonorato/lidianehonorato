
nome = str(input('digite seu nome:   '))
print('seu nome é: {}'.format(nome))
print('seu nome em maiuscula fica assim {}'.format(nome.upper()))
print('seu nome em minusculo fica assim {}'.format(nome.lower()))
print('seu nome em minusculo fica assim {}'.format(nome.title()))
print('seu nome tem {}'.format(len(nome) - nome.count(' ')))
#print('seu nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('seu nome {} e ele tem {} letras'.format(separa[0], len(separa[0])))



#frase= 'curso em video python'
#print(frase[::2])

