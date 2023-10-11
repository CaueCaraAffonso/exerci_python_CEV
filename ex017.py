#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

Ca = float(input('Digite o valor do cateto adjacente: '))
Co = float(input('Digite o valor do cateto oposto: '))
hip = math.hypot(Co, Ca)

print('O valor da hipotenusa é {:.2f} .'.format(hip))

