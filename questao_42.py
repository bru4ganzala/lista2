#42. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
#porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica.
#Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos de 45%,
#prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao
#consumidor

custo = float( input("Digite o custo de fábrica do carro: ") )

var1 = custo * 0.12
var2 = custo * 0.45

Valor = custo + var1 + var2

print ( f"o valor final do carro10 é :{Valor}")  