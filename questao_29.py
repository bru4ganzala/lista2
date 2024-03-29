#29. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que 
#solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que 
#deverá ser paga, sabendo-se que são descontados 11% de previdência social, e após 
#isso 8% para imposto de renda.

DIAS = input("Digite um número de dias de trabalho :")

SALARIO = DIAS * 30
SOCIAL =  SALARIO - (SALARIO * 0.11)
RENDA =  SOCIAL - (SOCIAL * 0.8)

print(f" O salalario liquido do funcionario é {RENDA}")
