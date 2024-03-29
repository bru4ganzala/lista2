#27. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo 
# que ele recebeu um monstruoso aumento de 1.77%.

SALARIO = float( input("Digite o seu saalrio: ") )

PORCENTAGEM = SALARIO * 0.0177
TOTAL = SALARIO + PORCENTAGEM

print (f" Seu salario ja adicionado seu mostruoso aumento de 1,77% e de : { TOTAL}")
