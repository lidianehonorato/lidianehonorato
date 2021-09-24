nome = str(input('qual o seu nome?   '))
if nome == 'jorge':
    print('nome lindo {}'.format(nome))
elif nome == ' souza  ' or nome == ' linhares ':
    print('seu nome nao é comum'.format(nome))
else:
      print('quem é voce {}? '.format(nome))

valor = float(input('qual o valor da casa?  '))
salario = float(input('qual o seu salario? '))
anos = int(input('quantos anos vc quer pagar? '))
prazo = valor / (anos * 12)
minino = salario * 30 / 100

print('para pagar a casa de R${:.2f} em {} anos '.format(prazo, anos))
print('vc pagara R$ {:.2f}'.format(prazo))
if prazo <= minino:
    print('emprestimo concedido')
else:
    print(' emprestimo nao concedido')