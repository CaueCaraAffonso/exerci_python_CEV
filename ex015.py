
#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia_aluguel = int(input('Por quantos dias o carro foi alugado?: '))
km_aluguel = float(input('Quantos quilometros o carro alugado percorreu?: '))

preço_dia = dia_aluguel*60
preço_km = km_aluguel*0.15

print('\n5O carro percorreu durante os {} dias de aluguel {} KM, resultando no total R${:.2f} . \n Sendo R${:.2f} pelos dias e R${:.2f} pelos quilometros andados.' .format(dia_aluguel , km_aluguel , preço_dia+preço_km , preço_dia , preço_km))

