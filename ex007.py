
#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
media_parcial = (nota1 + nota2 + nota3) / 3

print(
    "Suas notas respectivamente são {}, {}, {}.".format(nota1, nota2, nota3),
    end=" >>>>>>>> 3",
)
print("Sua média parcial é {:.1f}".format(media_parcial))
