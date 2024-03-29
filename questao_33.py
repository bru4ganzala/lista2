# 33. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
# subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para 
# atingir seu objetivo.

escada = float(input('Informe a altura de cada degrau da escada em metros: \n'))
altura = float(input('Informe a altura que você deseja chegar: \n'))

round=altura / escada, 2
print(f'Para chagar a altura desejada vc deverá subir {round} degraus')