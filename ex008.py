
#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = int(input("Escreva um valor em metros: "))

print(
    "O {} metros em centimetros é {}, e em milimetros é {}".format(
        metros, metros * 100, metros * 1000
    )
)
