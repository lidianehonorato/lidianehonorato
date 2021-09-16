
vl= float(input('qual a velocidade?  '))

if vl > 80:
    print('voce será multado, dirijindo acima de 80 KM/h, dirija com cautela!')
    multa = (vl - 80) * 7
    print('voce deve pagar o valor de R$ {:.2f}'.format(multa))
print('parabens voce é consciente, tenha um bom dia, dirija com seguranção!')
