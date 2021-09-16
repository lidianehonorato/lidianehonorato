from datetime import date

ano = int(input('qual o ano para analisar?  '))

if ano ==0: # se for digitado 0 atendera a condição
    ano = date.today().year #para analisar o ano atual

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('o ano {} é bissexto'.format(ano))
else: print('o ano {} não é bissexto'.format(ano))
