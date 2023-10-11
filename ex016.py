
#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num1 = float(input('Digite um número real com vírgula: '))
#numInteiro = trunc(num1)
print('O número {} tem a parte inteira {}'.format(num1, trunc(num1)))