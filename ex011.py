#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area_parede = altura*largura

print('A área da parede é {:.2f}m², então precisara de {:.0f} litros de tinta para pintar a parede inteira.'.format(area_parede , area_parede/2))