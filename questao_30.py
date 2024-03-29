#30. Faça um programa que leia o valor da hora de trabalho em reais e número de horas 
#trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre 
#o valor calculado.

VALOR= float(input('Digite o valor da hora trabalhada: \n'))
HORAS = float(input('Digite a quantidade de horas trabalhadas: \n'))

ADICIONAL = VALOR * HORAS * 0.1
TOTAL=VALOR* HORAS+ ADICIONAL

print(f'O valor a ser pago para o funcionário é:  {TOTAL}')