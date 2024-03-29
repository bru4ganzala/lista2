#44. Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês
#mais uma comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda. 
#Elabore um algoritmo para calcular e imprimir o salário do vendedor num dado mês 
#recebendo como dados de entrada o nome do vendedor, o número de carros vendidos 
#e o valor total das vendas.


nome = input("Digite seu nome:")
NCV = int( input("Digite a quantidae de carros vendidos : ") )
VTV = float( input("Digite o valor total das vendas: ") )

VLR_CARROS = NCV* 50.00
COMISSAO = VTV * 0.05

salario = VLR_CARROS + COMISSAO + 500

print ( f"{nome} seu salsrio será:{salario}")   