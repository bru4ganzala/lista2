# 32. Escreva um programa de ajuda para vendedor. A partir de um valor total lido mostre:
# a. O total a pagar com desconto de 10%;
# b. O valor de cada parcela, no parcelamento de 3x sem juros;
# c. A comissão do vendedor, caso de a venda ser a vista (5% sobre o valor com 
# desconto);
# d. A comissão do vendedor, caso de a venda ser parcelada (5% sobre o valor 
# total)

valor = float(input('Qual o valor total da compra: \n'))
desconto = valor * 0.1
print(f'Valor a vista com 10% de desconto: {valor - desconto} \n')
print(f'Valor parcelado em 3x - 1 de 3: {valor / 3}')
print(f'Valor parcelado em 3x - 2 de 3: {valor / 3}')
print(f'Valor parcelado em 3x - 3 de 3: {valor / 3} \n')
print(f'Comsissão para venda a vista: {round((valor - desconto) * 0.05, 2)} \n')
print(f'Comissão venda parcelada: {round(valor * 0.05, 2)}')