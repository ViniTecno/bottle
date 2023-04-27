#Resolução final

from pack.contas import *

while(True):
 exercicio=int(input('Digite qual exercicio você deseja escolher(1, 2, 3, 4, 5, 6 ou 7): '))
 print(exercicio)
 if exercicio==1:
     valor=float(input('Digite a metragem: '))
     resultado=metros_para_centimetros(valor)
     print(resultado)
     pass
 elif exercicio==2:
     horas=float(input('Digite quantas horas você trabalhou esse mês: '))
     ganhos=float(input('Digite quanto você ganha por hora: '))
     salário=ganho_por_hora(horas,ganhos)
     print(salário)
     pass
 elif exercicio==3:
     fahrenheit=float(input('Digite a temperatura em Fahrenheit: '))
     celsius=fahrenheit_para_celsius(fahrenheit)
     print('Temperatura em graus Celsius: ',celsius,'°')
     pass
 elif exercicio==4:

     pass
 elif exercicio==5:

     pass
 elif exercicio==6:

     pass
 elif exercicio==7:

     pass
 else: False    


    