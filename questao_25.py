#25. Leia a altura e raio de um cilindro circular e imprima o volume do cilindro. O volume de 
#um cilindro circular é calculado por meio da seguinte fórmula: 𝑉 = 𝜋 ∗ 𝑟𝑎𝑖𝑜² onde 𝜋 =
#3.141592.

ALTURA = float(input('Digite a altura do cilindro:'))
RAIO = float(input('Digite o raio do cilindro:'))

VOLUME = 3.141592 * (RAIO * RAIO)

print(f"O volume do silndro e igual a {VOLUME}")