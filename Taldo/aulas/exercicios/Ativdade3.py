#Crie um algoritmo que receba uma temperatura em Fahrenheit e converta para Celsius

from pack.contas import fahrenheit_para_celsius

fahrenheit=float(input('Digite a temperatura em Fahrenheit: '))
celsius=fahrenheit_para_celsius(fahrenheit)
print('Temperatura em graus Celsius: ',celsius,'°')