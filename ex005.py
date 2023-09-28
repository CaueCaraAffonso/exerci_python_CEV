
#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num1 = int(input('Digite um número: ')) #float para numero com virgula

print('O número escolhido é {}, o seu sucessor é {} e o seu antecessor é {}.' .format(num1, num1+1 , num1-1))