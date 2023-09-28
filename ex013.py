
# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_funcionario = float(input('Salário de um funcionário: '))
aumento_predefinido = float(salario_funcionario+(salario_funcionario*15/100))
aumento_salario = float(input('Qual a porcentagem de aumento ganho?: '))
salario_novo = float(salario_funcionario+(salario_funcionario*aumento_salario/100))

print('----'*5)
print('O salário R${} com 15% de aumento, fica R${:.2f} .'.format(salario_funcionario , aumento_predefinido))
print('----'*5)
print('O salário R${} com {}% de aumento, fica R${:.2f} .'.format(salario_funcionario , aumento_salario , salario_novo))
print('----'*5)
