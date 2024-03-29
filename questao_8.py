#8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
#fórmula de conversão é: 𝐶 = 𝐾 − 273.15, sendo 𝐶 a temperatura em Celsius e 𝐾 a 
#temperatura em Kelvin

KELVIN = float( input("Digite a temperatura em graus Kelvin: ") )
CELSIUS = KELVIN - 273.15

print ( f" A conversão para graus Celsius é: {CELSIUS}")   