from datetime import date

ano = int(input(' qual ano vc nasceu?  '))
atual = date.today().year
idade = atual - ano

print(' quem nasceu em {} tem {} anos em {}'. format(ano,idade,atual))
if idade == 18:
    print('aliste-se ')

