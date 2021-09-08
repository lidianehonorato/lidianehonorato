#mostrar algumas opçoes primitivas

a=input('digite algo  ')
print('o tipo primitivo é :  ',type(a))
print('so tem espaço? ',a.isspace())
print('é um numero? ', a.isnumeric())
print('é um decimal? ',a.isdecimal())
print('é alfabetico? ',a.isalpha())
print('é alfanumerico? ',a.isalnum())
print('tudo minusculo? ',a.islower())
print('tudo maiusculo?',a.isupper())
print('é capitalizado? ',a.title())

