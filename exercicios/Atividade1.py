#Crie um algoritmo que receba um valor em metros e converta para centímetros.

from pack.contas import metros_para_centimetros

valor=float(input('Digite a metragem: '))
resultado=metros_para_centimetros(valor)
print(resultado)