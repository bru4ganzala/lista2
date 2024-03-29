# 31. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, 
# sabendo-se que esse funcionário em uma gratificação de 5% sobre o salário-base. 
# Além disso, ele paga 7% de imposto sobre o salário-base.

SALARIO = input("Digite  o salario :")

GRATIFICACAO = SALARIO * 0.5
IMPOSTO = SALARIO * 0.7
TOTAL = SALARIO + GRATIFICACAO - IMPOSTO

print(f" O salalario liquido do funcionario é {TOTAL}")

