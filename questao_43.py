#43. O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a
#quantidade de cada item que você consumiu e calcule a conta final.
#a. Hambúrguer................. R$ 3,00
#b. Cheeseburger.............. R$ 2,50
#c. Fritas............................ R$ 2,50
#d. Refrigerante ................. R$ 1,00
#e. Milkshake..................... R$ 3,00A

H = int( input("Digite a quantidade de Hambúrguer consumidos: ") )
C = int( input("Digite a quantidade de Cheeseburger consumidos: ") )
F = int( input("Digite a quantidade de Fritas consumidos: ") )
R = int( input("Digite a quantidade de Refrigerante consumidos: ") )
M = int( input("Digite a quantidade de Milkshake consumidos: ") )

total = (H * 3.00) + (C * 2.50) + (F * 2.50) + (R * 1.00) + (M * 3.00)

print ( f"o valor total da conta é :{total}")  