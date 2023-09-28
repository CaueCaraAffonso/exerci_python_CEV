
#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

graus_celsius = float(input('Escreva um valor em graus Celsius: '))
graus_fahrenheit = 9/5*graus_celsius+32

print('o valor de {}° C em Fahrenheit é {}° F .'.format(graus_celsius , graus_fahrenheit))