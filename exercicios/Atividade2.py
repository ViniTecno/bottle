""" Crie um algoritmo que pergunte quanto você ganha por hora e o número de horas que você trabalha por mês, 
o algoritmo deve calcular e mostrar qual seu salário naquele mês """

from pack.contas import ganho_por_hora

horas=float(input('Digite quantas horas você trabalhou esse mês: '))
ganhos=float(input('Digite quanto você ganha por hora: '))
salário=ganho_por_hora(horas,ganhos)
print(salário)