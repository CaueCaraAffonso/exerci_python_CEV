
#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

texto = input('Escreva algo: ')

print('O que você escreveu é um {}!'.format(type(texto)))

print('É um número?', texto.isnumeric())
print('É um alfabético?', texto.isalpha())
print('Está tudo em minúsculo? ?', texto.islower())
print('Está tudo em maiúscula? ?', texto.isupper())
print('Tem espaço?', texto.isspace())
print('É alfanumérico?', texto.isalnum())
print('Está capitalizadaop? ?', texto.istitle())
