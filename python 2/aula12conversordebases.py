n = int(input('digite um numero  '))

print('''escolha uma das bases de conversão:
[ 1 ] para base binaria,
[ 2 ] para base hexadecimal,
[ 3 ] para base octal)''')
opçao = int(input('Sua opção ' ))

if opçao == 1:
    print(' {} convertido para binario é a {}'.format(n,bin(n)[2:]))
elif opçao == 2:
    print(' {} convertido para hexa é o {}'.format(n,hex(n)[2:]))
elif opçao == 3:
    print(' {} convertido para octal é o {}'.format(n,oct(n)[2:]))
else:
    print('opção invalida. tente novamente')
