#18. Sabendo que a formula para aprovação é: 𝐺1+(𝐺2∗2) 3 ≥ 7.0, desenvolva uma aplicação 
#que leia as notas de G1 e G2 e apresente a média do semestre.

G1 = float( input("Digite a nota da G1: ") )
G2 = float( input("Digite a nota da G2: ") )

SOMA = G1 + (G2 * 2)
MEDIA = SOMA / 3 

print ( f"A média do semestre é : {MEDIA}")   

