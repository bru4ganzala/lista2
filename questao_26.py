#26. Faça um programa que leia o valor de um produto e imprima o valor com desconto, 
#tendo em vista que o desconto foi de 12%

NUMERO = float( input("Digite o valor do produto: ") )

PORCENTAGEM = NUMERO * 0.12 
DESCONTO = NUMERO - PORCENTAGEM 

print (f"O valor de seu produto é { NUMERO } e o valor com o desconto é { DESCONTO}")

