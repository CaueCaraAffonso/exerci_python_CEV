# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite ângulo: '))

print('O SENO de {} é {:.2f}'.format(angulo , sin(radians(angulo))))
print('O COSSENO de {} é {:.2f}'.format(angulo , cos(radians(angulo))))
print('O TANGENTE de {} é {:.2f}'.format(angulo , tan(radians(angulo))))
