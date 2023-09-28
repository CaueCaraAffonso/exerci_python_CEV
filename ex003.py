
#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
soma = (num1 + num2)

print("")
#print('A soma de',num1,'+' ,num2, 'é igual à ',int(num1+num2))
#print('A soma é',int(num1+num2))

print("A soma de {} + {} é igual a {}!".format(num1, num2, soma))